import re


class SQLValidator:

    BLOCKED_KEYWORDS = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "TRUNCATE",
        "CREATE"
    ]

    @classmethod
    def validate(cls, sql: str):

        sql_upper = sql.upper()

        for keyword in cls.BLOCKED_KEYWORDS:
            if re.search(rf"\b{keyword}\b", sql_upper):
                raise ValueError(
                    f"Blocked SQL keyword: {keyword}"
                )

        return True