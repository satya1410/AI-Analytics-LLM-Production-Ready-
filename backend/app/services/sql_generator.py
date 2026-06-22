from app.services.ollama_service import OllamaService
from app.services.schema_service import SchemaService


class SQLGenerator:

    def __init__(self):
        self.ollama = OllamaService()

    def generate(self, question: str):

        schema = SchemaService.get_schema_context()

        with open(
            "app/prompts/sql/sql_generation.txt",
            "r"
        ) as f:
            prompt_template = f.read()

        prompt = prompt_template.format(
            schema=schema,
            question=question
        )

        sql = self.ollama.generate(prompt)

        return sql.strip()