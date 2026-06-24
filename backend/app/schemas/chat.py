# app/schemas/chat.py

from typing import Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    route: str
    answer: Optional[str]
    sql_result: Optional[dict]
    rag_result: Optional[dict]
    error: Optional[str]