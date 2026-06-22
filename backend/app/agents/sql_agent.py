from app.services.sql_generator import SQLGenerator
from app.services.sql_validator import SQLValidator
from app.services.sql_executor import SQLExecutor


class SQLAgent:

    def __init__(self):

        self.generator = SQLGenerator()

    def run(self, question: str):

        print(f"\nQuestion: {question}")

        sql = self.generator.generate(question)

        print(f"\nGenerated SQL:\n{sql}")

        SQLValidator.validate(sql)

        results = SQLExecutor.execute(sql)

        print(f"\nRows Returned: {len(results['rows'])}")

        return {
        "question": question,
        "sql": sql,
        "results": results
    }