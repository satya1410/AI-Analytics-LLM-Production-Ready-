# app/workflows/nodes/router_node.py

from app.services.ollama_service import OllamaService


ollama = OllamaService()


def router_node(state):

    question = state["question"]

    prompt = f"""
You are a routing agent.

Classify the user question into exactly one category.

SQL:
Questions about sales, profit, customers,
products, orders, revenue, analytics,
metrics, KPIs, trends.

RAG:
Questions about company policies,
documents, manuals, procedures,
employee information.

HYBRID:
Questions requiring both database analytics
and document knowledge.

Return ONLY one word:

SQL
RAG
HYBRID

Question:
{question}
"""

    route = ollama.generate(prompt).strip().upper()

    if route not in ["SQL", "RAG", "HYBRID"]:
        route = "RAG"

    state["route"] = route

    return state