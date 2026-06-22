from fastapi import APIRouter
from app.schemas.question import QuestionRequest
from app.agents.sql_agent import SQLAgent

router = APIRouter()

agent = SQLAgent()


@router.post("/ask")
def ask(request: QuestionRequest):

    return agent.run(request.question)