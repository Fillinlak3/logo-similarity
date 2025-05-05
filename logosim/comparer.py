# logosim/comparer.py

'''
    comparer.py – Groups visually similar logos based on perceptual hash distance.

    After downloading all the logos from the dataset,
    this script compares them by calculating the Hamming distance
    between their perceptual hashes (phash), with a configurable threshold (default: 8).

    Steps performed:
    - Loads image hashes from a JSON file
    - Computes pairwise Hamming distances between hashes
    - Groups together images with similar hashes (distance <= threshold)
    - Saves the resulting logo groups to output/groups.json

    This method avoids using heavy ML clustering algorithms and relies
    instead on lightweight distance-based grouping using image hashing.
'''

from logosim.utils import save_json, load_json, ensure_dir
from tqdm import tqdm
import os


# Load hashes of a `.json` file from `hashes_path`.
def load_hashes(hashes_path: str) -> dict:
    hashes = load_json(hashes_path)
    return hashes


# Calculate the hamming distance of 2 hashes.
def hamming_distance(hash1: str, hash2: str) -> int:
    return bin(int(hash1, 16) ^ int(hash2, 16)).count('1')


# Group similar images from a `hashes` dictionary into `output_dir`, using a configurable threshold.
def group_similar_images(hashes: dict, output_dir: str, threshold: int = 8) -> list:
    groups = []
    used = set()

    filenames = list(hashes.keys())

    # Only group unused hashes. If a hash is already used in a group, skip it.
    for i in tqdm(range(len(filenames)), desc="🔗 Grouping similar logos", dynamic_ncols=True):
        if filenames[i] in used:
            continue

        current_group = [filenames[i]]
        used.add(filenames[i])

        for j in range(i + 1, len(filenames)):
            if filenames[j] in used:
                continue

            distance = hamming_distance(hashes[filenames[i]], hashes[filenames[j]])

            if distance <= threshold:
                current_group.append(filenames[j])
                used.add(filenames[j])

        groups.append(current_group)

    save_groups(groups, output_dir)
    return groups


# Save `groups` list in a `.json` file into `save_dir`.
def save_groups(groups: list, save_dir: str) -> None:
    ensure_dir(save_dir)
    save_file = os.path.join(save_dir, "groups.json")

    save_json(groups, save_file)
    print(f"💾 Groups saved to {save_file}")


if __name__ == "__main__":
    hashes_path = "output/hashes.json"
    output_dir = "output"

    hashes = load_hashes(hashes_path)
    groups = group_similar_images(hashes, output_dir, threshold=8)

    print(f"✅ Grouped {len(hashes)} images into {len(groups)} groups.")
