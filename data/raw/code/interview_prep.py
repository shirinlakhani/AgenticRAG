"""
Interview Prep Notes
"""

# Core topics to review
TOPICS = [
    "Agentic AI vs Generative AI",
    "RAG architecture",
    "Vector databases and embeddings",
    "Prompt engineering best practices",
    "Multi-agent systems",
    "Production-grade deployment and governance"
]

# Example questions
QUESTIONS = [
    "Explain the core loop of an agentic AI system.",
    "How does RAG improve chatbot responses?",
    "What is the difference between a single-agent and multi-agent setup?",
    "How do you handle hallucinations in GenAI or Agentic AI?"
]

# Answers (brief)
ANSWERS = {
    "core_loop": "Perceive -> Reason & Plan -> Act -> Learn & Adapt",
    "RAG": "Retrieves relevant docs, then feeds to LLM to generate accurate answers",
    "single_vs_multi": "Single: sequential tasks; Multi: parallel specialized agents",
    "hallucinations": "Use retrieval, chain-of-thought reasoning, and human-in-the-loop validation"
}
