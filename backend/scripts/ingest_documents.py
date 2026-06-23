import uuid

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from app.services.document_loader import (
    DocumentLoader
)

from app.services.embedding_service import (
    EmbeddingService
)

from app.services.qdrant_service import (
    QdrantService
)


loader = DocumentLoader()

embedder = EmbeddingService()

qdrant = QdrantService()

qdrant.create_collection()

documents = loader.load_documents(
    "../data/documents"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

for document in documents:

    chunks = splitter.split_text(
        document["content"]
    )

    for idx, chunk in enumerate(chunks):

        embedding = embedder.embed(chunk)

        qdrant.insert_chunk(
            point_id=str(uuid.uuid4()),
            embedding=embedding,
            payload={
                "filename":
                    document["filename"],
                "chunk_id": idx,
                "text": chunk
            }
        )

print("Documents ingested")