# app/workflows/nodes/sql_node.py

from app.agents.sql_agent import SQLAgent

sql_agent = SQLAgent()


def sql_node(state):

    question = state["question"]

    try:
        result = sql_agent.run(question)

        state["sql_result"] = result

    except Exception as e:

        state["error"] = str(e)

    return state