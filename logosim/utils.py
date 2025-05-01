# logosim/utils.py

import os
import json
from typing import Any

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def save_json(data: Any, path: str) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def file_exists(path: str) -> bool:
    return os.path.isfile(path)

def path_is_empty(path: str) -> bool:
    return not(os.path.isdir(path) and len(os.listdir(path)) > 0)

def path_exists(path: str) -> bool:
    return os.path.exists(path)
