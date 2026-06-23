from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


class QdrantService:

    COLLECTION_NAME = "enterprise_documents"

    def __init__(self):

        self.client = QdrantClient(
            host="localhost",
            port=6333
        )

    def create_collection(self):

        collections = self.client.get_collections()

        existing = [
            c.name
            for c in collections.collections
        ]

        if self.COLLECTION_NAME not in existing:

            self.client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def insert_chunk(
        self,
        point_id,
        embedding,
        payload
    ):

        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=[
                PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload=payload
                )
            ]
        )

    def search(
        self,
        embedding,
        limit=5
    ):

        results = self.client.query_points(
            collection_name=self.COLLECTION_NAME,
            query=embedding,
            limit=limit
        )

        unique_points = []
        seen = set()

        for point in results.points:
            key = (
                point.payload.get("filename"),
                point.payload.get("chunk_id")
            )

            if key in seen:
                continue

            seen.add(key)
            unique_points.append(point)

        return unique_points