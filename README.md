
# AgenticRAG-Chatbot 


## **Overview**

AgenticRAG-Chatbot is a **Retrieval-Augmented Generation (RAG) chatbot** that leverages **Agentic AI, GenAI, LLMs, and prompt engineering** to answer questions about AI, cloud, and recommendation systems.  

The chatbot retrieves relevant knowledge from **CSV, PDF, Markdown, and code files** and provides **concise, accurate answers** using LLMs.  

This project is designed for:
- AI enthusiasts building **portfolio-ready RAG projects**
- Practicing **prompt engineering and multi-agent workflows**
- Demonstrating **recommendation system and AI knowledge**  

---

## **Project Structure**

```

AgenticRAG-Chatbot/
│
├─ data/
│   ├─ raw/             # Original CSVs, PDFs, markdowns, code
│   ├─ processed/       # Cleaned/preprocessed data
│   ├─ output/          # Generated outputs, logs
│   └─ embeddings/      # Vector DB files or embeddings
│
├─ src/                 # Core Python scripts
│   ├─ ingestion.py
│   ├─ embeddings.py
│   ├─ retrieval.py
│   ├─ agent.py
│   ├─ prompt_engine.py
│   └─ chatbot.py
│
├─ prompts/             # Prompt templates for the chatbot
├─ queries/             # Example queries + expected outputs
├─ requirements.txt
└─ README.md

````

---

## **Getting Started**

### **1. Clone the repository**

```bash
git clone https://github.com/shirinlakhani/AgenticRAG-Chatbot.git
cd AgenticRAG-Chatbot
````

### **2. Create a virtual environment and install dependencies**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### **3. Make sure Ollama is installed**

The chatbot uses **Ollama** to run LLMs locally. Download and install from: [https://ollama.com/](https://ollama.com/)

---

## **Running the Chatbot**

Run the chatbot script:

```bash
python src/chatbot.py
```

* The chatbot will read the **queries from `queries/` folder**, retrieve relevant information from `data/`, and generate responses using your LLM.
* Output JSONs are saved in `data/output/`.

---

## **Example Queries & Outputs**

| Query                 | Output                  |
| --------------------- | ----------------------- |
| `queries/query_1.txt` | `queries/output_1.json` |
| `queries/query_2.txt` | `queries/output_2.json` |
| `queries/query_3.txt` | `queries/output_3.json` |

**Example content:**

**Query:** `Explain what Retrieval-Augmented Generation (RAG) is and give an example of its application.`

**Chatbot Output:**

```json
{
  "query": "Explain what Retrieval-Augmented Generation (RAG) is and give an example of its application.",
  "response": "RAG combines retrieval from a knowledge base with LLM generation to provide accurate answers. For example, a RAG-based chatbot can answer AI interview questions by first retrieving relevant documents and then summarizing them using an LLM."
}
```

---

## **Folder Usage**

* **`data/raw/`** → store your original CSVs, PDFs, markdowns, code.
* **`data/processed/`** → store cleaned data ready for embeddings.
* **`data/embeddings/`** → store vector DB or embeddings.
* **`prompts/`** → store prompt templates for task decomposition, recommendations, or interview answers.
* **`queries/`** → store sample queries + expected outputs for testing and demos.




