# app/api/chat.py

from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.workflows.orchestrator import run_workflow

router = APIRouter(
    prefix="/api/v1",
    tags=["Chat"]
)


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    try:

        result = run_workflow(
            request.question
        )

        return ChatResponse(
            route=result.get("route"),
            answer=result.get("final_answer"),
            sql_result=result.get("sql_result"),
            rag_result=result.get("rag_result"),
            error=result.get("error"),
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )