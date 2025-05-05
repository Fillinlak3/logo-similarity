# logosim/main.py

'''
    main.py – Application entry point for the Logo Similarity project.

    This script builds the full pipeline of the project, step by step:

        1. Cleans any previous output directories (processed data and results)
        2. Loads the dataset from a `.parquet` file into a pandas DataFrame
        3. Downloads company favicons using the Google Favicon API (if not already downloaded)
        4. Processes all logos (grayscale + resized to 16x16)
        5. Computes perceptual hashes for the processed images
        6. Compares the hashes using Hamming distance and groups similar logos
        7. Saves the final groups to `output/groups.json`

    The pipeline avoids using heavy ML algorithms and instead relies on perceptual hashing and lightweight distance-based grouping.
    All important steps include validation to ensure data integrity before moving forward.
'''

from logosim.utils import path_exists, path_is_empty, file_exists
from logosim.loader import load_logos_data
from logosim.downloader import download_favicons
from logosim.processor import process_all_images, get_processed_images_hashes
from logosim.comparer import group_similar_images
from sys import exit as _sysexit

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="PIL")


if __name__ == "__main__":
    # 1. Clean directories.
    from shutil import rmtree as delete_path
    temporary_paths = ["data/processed", "output"]
    for path in temporary_paths:
        if path_exists(path):
            delete_path(path)

    # 2 & 3. Load and download logos if not done before.
    if path_is_empty("data/raw"):
        # II. Load logos from table.
        dataset_path = "data/logos.snappy.parquet"
        dataFrame_logos = load_logos_data(dataset_path)

        # Check if can continue after extracting the logos content from table.
        if dataFrame_logos.empty:
            print("❌ Data frame is empty. Cannot continue further.")
            _sysexit(1)

        # III. Download the logos.
        domains = dataFrame_logos["domain"].dropna().unique().tolist()
        download_favicons(domains, save_dir="data/raw")

        # ? Check if logos saved to `data/raw`.
        if path_is_empty("data/raw"):
            print("❌ No data saved/found in 'data/raw'. Cannot continue further.")
            _sysexit(1)

    # 4. Process the logos.
    processed_images = process_all_images(image_dir="data/raw", processed_dir="data/processed")
    image_hashes = get_processed_images_hashes(processed_images_dir="data/processed", output_dir="output")

    # Check if images were processed & saved into `output/hashes.json`.
    if not image_hashes or path_is_empty("data/processed") or not file_exists("output/hashes.json"):
        print("❌ No data saved/found in 'data/raw'. Cannot continue further.")
        _sysexit(1)

    # 5. Compare and group similar logos into clusters.
    groups = group_similar_images(image_hashes, output_dir="output")
    
    # Check if there are any groups & saved into `output/groups.json`.
    if not groups or not file_exists("output/groups.json"):
        print("❌ No groups found in 'data/processed'. Cannot continue further.")
        _sysexit(1)

    print(f"✅ Grouped {len(image_hashes)} images into {len(groups)} groups.")
