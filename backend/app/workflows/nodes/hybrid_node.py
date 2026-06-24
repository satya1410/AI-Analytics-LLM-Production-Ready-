# app/workflows/nodes/hybrid_node.py

from app.agents.sql_agent import SQLAgent
from app.agents.rag_agent import RAGAgent


sql_agent = SQLAgent()
rag_agent = RAGAgent()


def hybrid_node(state):

    question = state["question"]

    try:

        sql_result = sql_agent.run(question)

        rag_result = rag_agent.answer(question)

        state["sql_result"] = sql_result

        state["rag_result"] = rag_result

    except Exception as e:

        state["error"] = str(e)

    return state