# logosim/utils.py

'''
    utils.py – Globally used utility functions for file and path operations.

    This module provides helper functions that are used across multiple scripts in the project:
    
    - Creating directories if they don't exist (`ensure_dir`)
    - Saving and loading JSON files (`save_json`, `load_json`)
    - Checking for file and directory existence (`file_exists`, `path_exists`)
    - Checking if a directory is empty (`path_is_empty`)

    These small but essential utilities help ensure safe, readable, and reusable code throughout the entire pipeline.
'''

import os
import json
from typing import Any


# Creates the directory in `path` if it doesn't exist.
def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


# Save json `data` into `path` as a `.json` file.
def save_json(data: Any, path: str) -> None:
    ensure_dir(os.path.dirname(path))

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# Load the data from a `.json` file saved in `path`.
def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# Checks if the `path` to a file exists and it's a file (not a directory).
def file_exists(path: str) -> bool:
    return os.path.isfile(path)


# Checks if the given `path` is empty.
def path_is_empty(path: str) -> bool:
    return not(os.path.isdir(path) and len(os.listdir(path)) > 0)


# Checks if the given `path` exists.
def path_exists(path: str) -> bool:
    return os.path.exists(path)
