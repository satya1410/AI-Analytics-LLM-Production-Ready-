from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/enterprise_ai"
)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("Database connection successful")