from app.services.ollama_service import OllamaService
from app.services.schema_service import SchemaService
from pathlib import Path


class SQLGenerator:

    def __init__(self):
        self.ollama = OllamaService()

    def generate(self, question: str):

        schema = SchemaService.get_schema_context()

        prompt_path = (
            Path(__file__).resolve().parent.parent
            / "prompts"
            / "sql"
            / "sql_generation.txt"
        )

        with open(prompt_path, "r") as f:
            prompt_template = f.read()

        prompt = prompt_template.format(
            schema=schema,
            question=question
        )

        print("\n=== SQL AGENT PROMPT ===")
        print(prompt)

        sql = self.ollama.generate(prompt)

        print("\n=== GENERATED SQL ===")
        print(sql)

        return sql.strip()