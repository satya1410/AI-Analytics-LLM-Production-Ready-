# app/workflows/nodes/synthesis_node.py

from app.services.ollama_service import OllamaService


ollama = OllamaService()


def synthesis_node(state):

    question = state["question"]

    sql_result = state.get("sql_result")

    rag_result = state.get("rag_result")

    prompt = f"""
You are an Enterprise Analytics Assistant.

Question:
{question}

SQL Results:
{sql_result}

RAG Results:
{rag_result}

Generate a concise and professional answer.

If one section is missing,
ignore it.
"""

    answer = ollama.generate(prompt)

    state["final_answer"] = answer

    return state