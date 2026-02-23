# src/ingestion/pdf_parser.py

import os
import pdfplumber

def extract_text_from_pdf(input_dir: str, output_dir: str):
    """
    Extracts text from all PDFs in input_dir and saves as plain text in output_dir.
    """
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            file_path = os.path.join(input_dir, filename)
            with pdfplumber.open(file_path) as pdf:
                text = "\n".join([page.extract_text() or "" for page in pdf.pages])

            # Clean extra whitespace
            text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])

            output_file = os.path.join(output_dir, filename.replace(".pdf", ".txt"))
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"[PDF] Processed: {output_file}")


if __name__ == "__main__":
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))
    extract_text_from_pdf(
        input_dir=os.path.join(BASE_DIR, "raw/pdfs"),
        output_dir=os.path.join(BASE_DIR, "processed/pdfs")
    )
