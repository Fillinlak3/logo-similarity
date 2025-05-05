# logosim/loader.py

'''
    loader.py – Loads the input dataset from a Parquet file into a pandas DataFrame.

    This module is responsible for reading the list of company domains
    from the provided `.parquet` dataset using the pandas library.

    Steps performed:
    - Loads the dataset from a given path (`data/logos.snappy.parquet`)
    - Displays basic metadata: number of rows, columns, preview
    - Returns a pandas `DataFrame` for downstream processing

    In case of failure, an empty DataFrame is returned and an error is logged.
'''

import pandas as pd

def load_logos_data(dataset_path: str) -> pd.DataFrame:
    print(f"🔍 Loading data from {dataset_path}...")
    try:
        dataFrame = pd.read_parquet(dataset_path)
        print("✅ Data loaded successfully!")
        print(f"📊 Number of rows: {len(dataFrame)}")
        print("\n📌 Available columns:")
        print(dataFrame.columns.tolist())
        print("\n🔎 Preview (first 5):")
        print(dataFrame.head(5))
        return dataFrame
    
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        return pd.DataFrame()