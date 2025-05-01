# logosim/comparer.py

import os
import json
from tqdm import tqdm

def load_hashes(hashes_path: str) -> dict:
    with open(hashes_path, "r") as f:
        hashes = json.load(f)
    return hashes

def hamming_distance(hash1: str, hash2: str) -> int:
    return bin(int(hash1, 16) ^ int(hash2, 16)).count('1')

def group_similar_images(hashes: dict, output_dir: str, threshold: int = 8) -> list:
    groups = []
    used = set()

    filenames = list(hashes.keys())

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

def save_groups(groups: list, save_dir: str) -> None:
    save_file = os.path.join(save_dir, "groups.json")
    os.makedirs(os.path.dirname(save_file), exist_ok=True)

    with open(save_file, "w") as f:
        json.dump(groups, f, indent=4)
    print(f"💾 Groups saved to {save_file}")

if __name__ == "__main__":
    hashes_path = "output/hashes.json"
    output_dir = "output"

    hashes = load_hashes(hashes_path)
    groups = group_similar_images(hashes, output_dir, threshold=8)

    print(f"✅ Grouped {len(hashes)} images into {len(groups)} groups.")
