# logosim/processor.py

import os
import json
from PIL import Image
import imagehash
from tqdm import tqdm
from shutil import rmtree

def process_image(image_path: str, hash_size: int = 16) -> Image:
    try:
        with Image.open(image_path) as img:
            img = img.convert("L")  # grayscale
            img = img.resize((hash_size, hash_size))
            return img.copy()
    except Exception as e:
        tqdm.write(f"❌ Failed processing {image_path}: {e}")
        return None
    
def get_image_hash(image_path: str) -> str:
    try:
        with Image.open(image_path) as img:
            hash_value = imagehash.phash(img)
            return str(hash_value)
    except Exception as e:
        tqdm.write(f"❌ Failed getting hash for {image_path}: {e}")
        return None

def process_all_images(image_dir: str, processed_dir: str, hash_size: int = 16) -> dict:
    images = {}
    files = os.listdir(image_dir)

    for filename in tqdm(files, desc="⚙️ Processing images", dynamic_ncols=True):
        file_path = os.path.join(image_dir, filename)

        if os.path.isfile(file_path):
            img = process_image(file_path, hash_size=hash_size)
            if img:
                images[filename] = img

    save_processed_images(images, processed_dir)
    return images

def get_processed_images_hashes(processed_images_dir: str, output_dir: str) -> dict:
    image_hashes = {}
    files = os.listdir(processed_images_dir)

    for filename in tqdm(files, desc="⚙️ Getting hashes", dynamic_ncols=True):
        file_path = os.path.join(processed_images_dir, filename)

        if os.path.isfile(file_path):
            hash_value = get_image_hash(file_path)
            if hash_value:
                image_hashes[filename] = hash_value

    save_hashes(image_hashes, output_dir)
    return image_hashes

def save_processed_images(images: dict, save_dir: str, format: str = "png") -> None:
    os.makedirs(save_dir, exist_ok=True)

    for filename, image in images.items():
        try:
            # te asiguri că extensia e corectă (png sau jpg)
            clean_name = os.path.splitext(filename)[0]
            save_path = os.path.join(save_dir, f"{clean_name}.{format}")
            image.save(save_path, format=format.upper())
        except Exception as e:
            print(f"❌ Could not save {filename}: {e}")

    print(f"💾 Saved {len(images)} images to {save_dir}")

def save_hashes(hashes: dict, save_path: str) -> None:
    save_file = os.path.join(save_path, "hashes.json")
    os.makedirs(os.path.dirname(save_file), exist_ok=True)

    with open(save_file, "w") as f:
        json.dump(hashes, f, indent=4)
    print(f"💾 Hashes saved to {save_file}")

if __name__ == "__main__":
    image_dir = "data/raw/"
    processed_dir = "data/processed"
    output_path = "output"
    
    rmtree(processed_dir)
    processed_images = process_all_images(image_dir, processed_dir)
    hashes = get_processed_images_hashes(processed_dir, output_path)

    print(f"✅ Processed and saved {len(hashes)} hashes.")
