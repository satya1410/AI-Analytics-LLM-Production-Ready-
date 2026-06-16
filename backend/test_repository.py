from app.core.database import SessionLocal
from app.repositories.order_repository import OrderRepository

db = SessionLocal()

try:
    repo = OrderRepository(db)

    print(
        f"Orders count: {repo.count()}"
    )

finally:
    db.close()
    