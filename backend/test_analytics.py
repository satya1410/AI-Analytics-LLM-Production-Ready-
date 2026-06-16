from app.core.database import SessionLocal
from app.services.analytics_service import AnalyticsService

db = SessionLocal()

try:
    service = AnalyticsService(db)

    results = service.top_products()

    for product, profit in results:
        print(product, profit)

finally:
    db.close()