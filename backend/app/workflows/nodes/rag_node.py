# app/workflows/nodes/rag_node.py

from app.agents.rag_agent import RAGAgent

rag_agent = RAGAgent()


def rag_node(state):

    question = state["question"]

    try:

        result = rag_agent.answer(question)

        state["rag_result"] = result

    except Exception as e:

        state["error"] = str(e)

    return state