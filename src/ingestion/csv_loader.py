# src/ingestion/csv_loader.py

import os
import pandas as pd

def load_and_process_csv(input_dir: str, output_dir: str):
    """
    Loads all CSV files from input_dir, cleans/processes them,
    and saves processed CSVs to output_dir.
    """
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_dir, filename)
            df = pd.read_csv(file_path)

            # Example processing: drop empty rows, strip whitespace from strings
            df = df.dropna().applymap(lambda x: x.strip() if isinstance(x, str) else x)

            output_file = os.path.join(output_dir, filename)
            df.to_csv(output_file, index=False)
            print(f"[CSV] Processed: {output_file}")


if __name__ == "__main__":
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))
    load_and_process_csv(
        input_dir=os.path.join(BASE_DIR, "raw/csvs"),
        output_dir=os.path.join(BASE_DIR, "processed/csvs")
    )
