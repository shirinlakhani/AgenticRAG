
# AgenticRAG

## Project Overview
**AgenticRAG** is an **AI Knowledge Assistant** that leverages **RAG (Retrieval-Augmented Generation)**, **Agentic AI**, and **Model Context Protocol (MCP)** to answer technical and interview questions about Generative AI and Agentic AI.

It leverages internal knowledge sources (PDFs, markdowns, CSVs) to provide accurate, context-aware, and actionable answers, using multi-agent orchestration and structured memory.

### Key Features
- **Retrieval from multiple knowledge sources:** PDF, Markdown, CSV  
- **Agentic AI:** Implements a **Perceive → Reason → Act → Learn** loop  
- **Task Decomposition:** Handles multi-step workflows  
- **Prompt Optimization:** Refines logic for superior AI output  
- **MCP-Enabled:** Context management and tool calling via [Model Context Protocol](https://modelcontextprotocol.io)  
- **Vector Search:** Embeddings management with [FAISS](https://github.com) or [Chroma](https://www.trychroma.com)  
- **Multi-Agent Orchestration:** Tool-using LLM agents  
- **API Deployment:** Interact via FastAPI endpoints  
- **Docker Ready:** Containerized for consistent deployment

---

## Folder Structure

```text
AgenticRAG/
├── data/
│   ├── raw/
│   │   ├── code/
│   │   ├── csvs/
│   │   ├── markdowns/
│   │   └── pdfs/
│   ├── processed/
│   └── embeddings/
├── prompts/                   # System prompts and templates
├── notebooks/                 # Experimentation only
├── queries/                   # Example questions & tests
├── src/
│   ├── agent/
│   │   ├── agent_core.py
│   │   ├── rag_engine.py
│   │   └── prompt_manager.py
│   ├── api/
│   │   └── app.py             # FastAPI endpoints
│   ├── ingestion/             # Data parsers and loaders
│   ├── embeddings/            # Embedding generator scripts
│   └── utils/                 # Helpers: logging, config, etc.
├── tests/
├── output/
├── requirements.txt
└── README.md

```

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
4. **Agent** – Implements multi-agent orchestration and reasoning loops.  
5. **Utils** – Helper functions for text cleaning, logging, and configuration.  

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
```
---

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```
---

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

3. **Launch FastAPI Server:**

   ```bash
   uvicorn src.api.app:app --reload
   ```
Access the API at http://127.0.0.1:8000

4. **POST a JSON to /ask endpoint:**

```json
{
  "question": "Explain RAG Architecture"
}
```

5. **Experiment with Notebooks:**

   ```bash
   jupyter notebook notebooks/rag_demo.ipynb
   ```

---

## Docker Deployment

### 1. Create a `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
```
### 2. Build Docker image
```bash
docker build -t agenticrag:latest .
```

### 3. Run container
```bash
docker run -p 8000:8000 agenticrag:latest
```


## Best Practices

- **Organized Prompts:** Store all prompt templates in `prompts/` for reproducibility.  
- **Unit Tests:** Use `tests/` to validate ingestion, embeddings, and retrieval logic.  
- **Version Control:** Track changes in raw data and code using Git.  
- **Human-in-the-Loop:** Ensure high-risk answers are reviewed before deployment.  
- **Observability:** Log embeddings, queries, and retrieval results for debugging.  

---

## Skills Highlighted

- **AI Strategy:** Prompt Engineering, Agentic Workflow Design, RAG Architecture  
- **AI Frameworks:** LangChain, LangGraph, CrewAI, LlamaIndex, Flowise/LangFlow  
- **Technical Implementation:** GitHub Copilot, Python, Vector DBs (FAISS, Chroma, Pinecone), API Integration (OpenAI, Ollama, Anthropic)  
- **Context Engineering & MCP:** Multi-agent orchestration and memory management  

---

## Sample Prompts

***task_decomposition.txt***

```text
Given the high-level goal: {goal}, break it down into actionable steps.
Use reasoning loops (Perceive → Reason → Act → Learn) and MCP for context management.
```
---
***system_agentic.txt***

```text
You are an Agentic AI system capable of multi-step tasks.
Interact with APIs, databases, and other agents.
Maintain context with MCP, manage memory, and learn from failures.
```

***rag_retrieval_prompt.txt***

```text
You are an AI assistant specializing in Agentic AI, GenAI, RAG, and MCP.
Answer the question: {user_question} using the retrieved context {retrieved_context}.
If no relevant info is found, reply: "I could not find sufficient information in the knowledge base."
```
## Raw Data Examples

**CSV (`data/raw/csvs/knowledge_base.csv`)**

| topic              | content                                                |
| ------------------ | ------------------------------------------------------ |
| RAG Architecture   | Retrieval-Augmented Generation (RAG) is a pipeline ... |
| Prompt Engineering | Effective prompts improve LLM responses by ...         |

**Markdown (`data/raw/markdowns/AgenticAI_GenAI.md`)**

```markdown
# Agentic AI & Generative AI Overview
Agentic AI acts autonomously using Perceive → Reason → Act → Learn loops.
Generative AI creates outputs like text, code, and images.
RAG combines embeddings with LLMs for contextual answers.
MCP manages context and memory for multi-agent orchestration.
```
## PDFs (`data/raw/pdfs/`)
Technical reference documents for Agentic AI, GenAI, and RAG concepts.

---

## Next Steps / Roadmap

- **Ingestion:** Parse and clean PDFs, markdowns, and CSVs  
- **Embeddings:** Generate vector representations  
- **RAG:** Implement retrieval-augmented generation  
- **Agent:** Build Agentic AI loop (Perceive → Reason → Act → Learn)  
- **MCP:** Enable structured context, memory, and tool orchestration  
- **API:** Expose via FastAPI for integration  

---

## Key Notes

- **ATS-friendly:** Focus on RAG, MCP, Agentic AI, Prompt Engineering  
- **Demoable:** Query → retrieval → stepwise reasoning  
- **Non-heavy coding:** Python + Copilot-assisted scripts  
- **Domain-relevant:** Enterprise SaaS, Healthcare, FinTech, HR, Legal, AI startups  
- **API-first & Deployable:** REST endpoints, modular structure, FastAPI-ready

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

