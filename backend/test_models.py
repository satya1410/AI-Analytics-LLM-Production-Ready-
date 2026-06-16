from sqlalchemy import text

from app.core.database import SessionLocal

db = SessionLocal()

try:
    result = db.execute(
        text("SELECT COUNT(*) FROM orders")
    )

    count = result.scalar()

    print(f"Orders: {count}")

finally:
    db.close()