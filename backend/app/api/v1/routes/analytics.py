from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/top-products")
def top_products(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    service = AnalyticsService(db)

    results = service.top_products(limit)

    return [
        {
            "product_name": product_name,
            "profit": float(profit)
        }
        for product_name, profit in results
    ]