from fastapi import FastAPI

from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.analytics import router as analytics_router

app = FastAPI(
    title="Enterprise AI Analytics Agent",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(analytics_router)

@app.get("/")
def root():
    return {
        "message": "Enterprise AI Analytics Agent"
    }