# src/ingestion/markdown_parser.py

import os

def parse_markdown(input_dir: str, output_dir: str):
    """
    Loads all Markdown files from input_dir, extracts text,
    and saves as plain text in output_dir.
    """
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Example processing: remove extra whitespace
            content = "\n".join([line.strip() for line in content.splitlines() if line.strip()])

            output_file = os.path.join(output_dir, filename.replace(".md", ".txt"))
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"[Markdown] Processed: {output_file}")


if __name__ == "__main__":
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))
    parse_markdown(
        input_dir=os.path.join(BASE_DIR, "raw/markdowns"),
        output_dir=os.path.join(BASE_DIR, "processed/markdowns")
    )
