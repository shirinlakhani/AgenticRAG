"""
RAG (Retrieval-Augmented Generation) Concepts
"""

# Definition
RAG_DEFINITION = """
RAG combines a retrieval system (vector DB, knowledge base) with a generative model.
It allows chatbots to answer questions using external sources, not just LLM memory.
"""

# Workflow
RAG_WORKFLOW = [
    "Query understanding (NLP processing)",
    "Retrieve relevant documents from vector DB",
    "Feed retrieved content to LLM",
    "Generate accurate, context-aware answer"
]

# Vectorstore examples
VECTORSTORES = ["Chroma", "Pinecone", "Weaviate", "FAISS"]
