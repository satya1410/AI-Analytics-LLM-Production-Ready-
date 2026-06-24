from fastapi import FastAPI

from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.analytics import router as analytics_router
from app.api.v1.routes.ask import router as ask_router
from app.api.v1.routes import rag
from app.api.chat import router as chat_router

app = FastAPI(
    title="Enterprise AI Analytics Agent",
    version="1.0.0"
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    analytics_router,
    prefix="/api/v1",
    tags=["Analytics"]
)

app.include_router(
    ask_router,
    prefix="/api/v1",
    tags=["SQL Agent"]
)

app.include_router(
    rag.router,
    prefix="/api/v1",
    tags=["RAG Agent"]
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "Enterprise AI Analytics Agent"
    }