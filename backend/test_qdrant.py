from app.services.qdrant_service import QdrantService

service = QdrantService()

service.create_collection()

print("Collection created")