import ollama


class OllamaService:

    def generate(
        self,
        prompt: str,
        model: str = "llama3.2"
    ):
        response = ollama.generate(
            model=model,
            prompt=prompt
        )

        return response["response"]