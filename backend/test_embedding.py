from app.services.embedding_service import EmbeddingService

service = EmbeddingService()

embedding = service.embed("What is the return policy?")

print(len(embedding))