# logosim/main.py

from logosim.utils import path_exists, path_is_empty, file_exists
from logosim.loader import load_logos_data
from logosim.downloader import download_favicons
from logosim.processor import process_all_images, get_processed_images_hashes
from logosim.comparer import group_similar_images
from sys import exit as _sysexit

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="PIL")

if __name__ == "__main__":
    # 1. Clean paths.
    from shutil import rmtree as delete_path
    temporary_paths = ["data/processed", "output"]
    for path in temporary_paths:
        if path_exists(path):
            delete_path(path)

    # 2 & 3. Load and download logos if not done before.
    if path_is_empty("data/raw"):
        # 2. Load logos from table.
        FILEPATH = "data/logos.snappy.parquet"
        dataFrame_logos = load_logos_data(FILEPATH)

        # Check if can continue after extracting the logos content from table.
        if dataFrame_logos.empty:
            print("❌ Data frame is empty. Cannot continue further.")
            _sysexit(1)

        # 3. Download the logos.
        domains = dataFrame_logos["domain"].dropna().unique().tolist()
        download_favicons(domains, save_dir="data/raw")

        # Check if logos saved to 'data/raw'
        if path_is_empty("data/raw"):
            print("❌ No data saved/found in 'data/raw'. Cannot continue further.")
            _sysexit(1)

    # 4. Process the logos.
    processed_images = process_all_images(image_dir="data/raw", processed_dir="data/processed")
    image_hashes = get_processed_images_hashes(processed_images_dir="data/processed", output_dir="output")

    # Check if images were processed & saved into 'output/hashes.json'
    if not image_hashes or path_is_empty("data/processed") or not file_exists("output/hashes.json"):
        print("❌ No data saved/found in 'data/raw'. Cannot continue further.")
        _sysexit(1)

    # 5. Compare the logos.
    groups = group_similar_images(image_hashes, output_dir="output")
    
    if not groups or not file_exists("output/groups.json"):
        print("❌ No groups found in 'data/processed'. Cannot continue further.")
        _sysexit(1)
    else:
        print(f"✅ Grouped {len(image_hashes)} images into {len(groups)} groups.")
