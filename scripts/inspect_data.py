import pandas as pd
from pathlib import Path

file_path = Path("data/Global_Superstore2.csv")

print(f"Reading file: {file_path.resolve()}")

encodings = ["utf-8", "latin1", "cp1252"]

df = None
for enc in encodings:
    try:
        print(f"Trying encoding: {enc}")
        df = pd.read_csv(file_path, encoding=enc)
        print(f"Successfully loaded using {enc}")
        break
    except UnicodeDecodeError:
        continue

if df is None:
    raise ValueError("Could not read CSV with utf-8, latin1, or cp1252 encodings")

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())