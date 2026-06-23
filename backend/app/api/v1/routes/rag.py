from fastapi import APIRouter

from app.schemas.question import (
    QuestionRequest
)

from app.agents.rag_agent import (
    RAGAgent
)

router = APIRouter()

agent = RAGAgent()


@router.post("/rag")
def ask_rag(
    request: QuestionRequest
):

    return agent.answer(
        request.question
    )