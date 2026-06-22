from sqlalchemy import text
from app.core.database import SessionLocal


class SQLExecutor:

    @staticmethod
    def execute(sql: str):

        db = SessionLocal()

        try:

            result = db.execute(text(sql))

            rows = result.fetchall()

            columns = result.keys()

            return {
                "columns": list(columns),
                "rows": [list(row) for row in rows]
            }

        finally:
            db.close()