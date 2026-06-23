from pathlib import Path

from app.services.embedding_service import (
    EmbeddingService
)

from app.services.qdrant_service import (
    QdrantService
)

from app.services.ollama_service import (
    OllamaService
)


class RAGAgent:

    def __init__(self):

        self.embedder = EmbeddingService()

        self.qdrant = QdrantService()

        self.ollama = OllamaService()

        prompt_path = (
            Path(__file__).resolve().parents[1]
            / "prompts"
            / "rag"
            / "rag_prompt.txt"
        )

        self.rag_prompt = prompt_path.read_text(
            encoding="utf-8"
        )

    def answer(self, question):

        query_embedding = self.embedder.embed(
            question
        )

        chunks = self.qdrant.search(
            query_embedding
        )

        chunks = [
            hit
            for hit in chunks
            if getattr(hit, "score", 0) >= 0.6
        ]

        if not chunks:
            return {
                "answer": (
                    "I cannot find that information "
                    "in the provided documents."
                ),
                "sources": []
            }

        context = "\n\n".join(
            hit.payload["text"]
            for hit in chunks
        )

        prompt = self.rag_prompt.format(
            context=context,
            question=question
        )

        answer = self.ollama.generate(
            prompt
        )

        unique_sources = []
        seen = set()

        for hit in chunks:
            source_key = (
                hit.payload.get("filename"),
                hit.payload.get("chunk_id")
            )

            if source_key in seen:
                continue

            seen.add(source_key)

            unique_sources.append(
                {
                    "file": hit.payload["filename"],
                    "chunk_id": hit.payload.get(
                        "chunk_id"
                    ),
                    "score": hit.score
                }
            )

        return {
            "answer": answer,
            "sources": unique_sources
        }