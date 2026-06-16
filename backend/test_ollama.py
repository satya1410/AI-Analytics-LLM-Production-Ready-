from app.services.ollama_service import OllamaService

service = OllamaService()

response = service.generate(
    "Explain SQL agents in one paragraph."
)

print(response)