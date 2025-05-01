# logosim/downloader.py

from logosim.utils import ensure_dir
import requests
from tqdm import tqdm
from sys import exit as _sysexit
import os

def build_favicon_url(domain: str, size: int = 64) -> str:
    return f"https://www.google.com/s2/favicons?sz={size}&domain={domain}"

def download_image(url: str, save_path: str) -> bool:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(response.content)
        return True
    except Exception as e:
        tqdm.write(f"❌ Failed to download {url}: {e}")
        return False

def download_favicons(domains: list[str], save_dir: str, size: int = 64) -> None:
    ensure_dir(save_dir)
    ensure_dir("output")

    failed = []

    for domain in tqdm(domains, desc="⬇️ Downloading favicons", dynamic_ncols=True):
        url = build_favicon_url(domain, size=size)
        filename = domain.replace("/", "_") + ".png"
        path = os.path.join(save_dir, filename)

        success = download_image(url, path)
        if not success:
            failed.append(domain)

    if failed:
        failed_log_path = os.path.join("output", "failed_downloads.txt")
        with open(failed_log_path, "w") as f:
            for domain in failed:
                f.write(domain + "\n")
        print(f"⚠️ {len(failed)} downloads failed. Check '{failed_log_path}'.")

if __name__ == "__main__":
    from logosim.loader import load_logos_data

    dataFrame_logos = load_logos_data("data/logos.snappy.parquet")

    # Firstly, check if we can continue after extracting the logos content from '.parquet' file.
    if dataFrame_logos.empty:
        print("❌ Data frame is empty, cannot continue further.")
        _sysexit(1)

    domains = dataFrame_logos["domain"].dropna().unique().tolist()
    download_favicons(domains, save_dir="data/raw/")
