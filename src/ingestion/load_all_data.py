# src/ingestion/load_all_data.py

from ingestion.csv_loader import load_and_process_csv
from ingestion.markdown_parser import parse_markdown
from ingestion.pdf_parser import extract_text_from_pdf
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))

def load_all_data():
    load_and_process_csv(
        input_dir=os.path.join(BASE_DIR, "raw/csvs"),
        output_dir=os.path.join(BASE_DIR, "processed/csvs")
    )
    parse_markdown(
        input_dir=os.path.join(BASE_DIR, "raw/markdowns"),
        output_dir=os.path.join(BASE_DIR, "processed/markdowns")
    )
    extract_text_from_pdf(
        input_dir=os.path.join(BASE_DIR, "raw/pdfs"),
        output_dir=os.path.join(BASE_DIR, "processed/pdfs")
    )
    print("✅ All data processed successfully!")


if __name__ == "__main__":
    load_all_data()
