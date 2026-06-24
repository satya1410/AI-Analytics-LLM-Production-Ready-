from typing import TypedDict


class AgentState(TypedDict):
    question: str

    route: str

    sql_result: dict | None

    rag_result: dict | None

    final_answer: str