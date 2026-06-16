from app.core.database import SessionLocal

db = SessionLocal()

try:
    print("Session created successfully")
finally:
    db.close()