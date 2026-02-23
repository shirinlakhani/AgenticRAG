
# AgenticRAG-Chatbot

## Overview
The **AgenticRAG-Chatbot** project is a Retrieval-Augmented Generation (RAG) system designed to answer questions related to **AI, Generative AI (GenAI), Agentic AI, and Prompt Engineering**. This repository integrates multiple data sources including PDFs, CSVs, and Markdown documents, converts them into vector embeddings, and leverages LLMs to generate accurate and context-aware responses.

This project is structured to be **modular, scalable, and production-ready**, making it ideal for experimentation, learning, and professional interviews.

---

## Folder Structure

```

AgenticRAG-Chatbot/
├── data/
│   ├── raw/
│   │   ├── code/                  # Raw reference code files
│   │   ├── csvs/                  # Raw CSV knowledge bases
│   │   ├── markdowns/             # Raw markdown documentation
│   │   └── pdfs/                  # Raw PDF documents
│   ├── processed/                 # Cleaned / tokenized / parsed data
│   └── embeddings/                # Generated vector embeddings
├── prompts/                       # Predefined prompts / example queries
├── notebooks/                      # Jupyter notebooks for experimentation
├── src/                            # Source code
│   ├── ingestion/                 # Scripts to process raw data
│   ├── embeddings/                # Scripts to generate/store embeddings
│   ├── rag/                       # Core RAG chatbot code
│   └── utils/                     # Utility functions
├── tests/                          # Unit tests for each module
├── output/                         # Logs, chatbot output, debug results
├── requirements.txt                # Python dependencies
└── README.md                        # Project documentation

````

---

## Key Components

### Data
- **Raw Data:** PDFs, Markdown files, CSVs containing knowledge sources.
- **Processed Data:** Tokenized and cleaned text ready for embedding.
- **Embeddings:** Vector representations used by the RAG engine for retrieval.

### Prompts
- Predefined system prompts and example queries for consistent AI responses.
- Organized by topics: `GenAI`, `Agentic AI`, `RAG`, and `Prompt Engineering`.

### Source Code (`src/`)
1. **Ingestion** – Scripts to load and parse raw data.
2. **Embeddings** – Scripts to generate embeddings using models like OpenAI, Ollama, or local LLMs.
3. **RAG Engine** – Core retrieval and answer generation code.
4. **Utils** – Helper functions for text cleaning, logging, and configuration.

### Notebooks
- `rag_demo.ipynb` for testing workflows, visualizing embeddings, and iterating on prompts.

### Tests
- Unit tests for ingestion, embedding generation, and RAG engine to ensure correctness.

### Output
- Stores logs, intermediate results, and final chatbot responses for debugging and evaluation.

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd AgenticRAG-Chatbot
````

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. **Ingest Data:**

   ```bash
   python src/ingestion/pdf_parser.py
   python src/ingestion/markdown_parser.py
   python src/ingestion/csv_loader.py
   ```

2. **Generate Embeddings:**

   ```bash
   python src/embeddings/embedding_generator.py
   ```

3. **Run Chatbot:**

   ```bash
   python src/rag/rag_engine.py
   ```

4. **Experiment with Notebooks:**

   ```bash
   jupyter notebook notebooks/rag_demo.ipynb
   ```

---

## Best Practices

* **Organized Prompts:** Store all prompt templates in `prompts/` for reproducibility.
* **Unit Tests:** Use `tests/` to validate ingestion, embeddings, and retrieval logic.
* **Version Control:** Track changes in raw data and code using Git.
* **Human-in-the-loop:** Ensure high-risk answers are reviewed before deployment.
* **Observability:** Log embeddings, queries, and retrieval results for debugging.

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to branch: `git push origin feature/my-feature`
5. Create a pull request.

---

## License

This project is licensed under the MIT License.

---

## References

* **Generative AI & Agentic AI:** Gartner, AWS, Exabeam, OpenAI, Ollama
* **RAG Systems:** LangChain, LlamaIndex, Microsoft AutoGen
* **Python Libraries:** pandas, numpy, PyPDF2, FAISS, Chroma, Streamlit, Gradio

