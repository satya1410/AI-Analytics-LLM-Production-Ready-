from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/enterprise_ai"

engine = create_engine(DATABASE_URL)


def get_engine():
    return engine