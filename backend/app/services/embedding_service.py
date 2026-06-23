from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def embed(self, text: str):
        embedding = self.model.encode(text)
        return embedding.tolist()

    def embed_batch(self, texts: list[str]):
        embeddings = self.model.encode(texts)
        return embeddings.tolist()