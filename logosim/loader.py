# logosim/loader.py

import pandas as pd

def load_logos_data(filepath: str) -> pd.DataFrame:
    print(f"🔍 Loading data from {filepath}...")
    try:
        dataFrame = pd.read_parquet(filepath)
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