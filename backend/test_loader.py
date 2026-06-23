from app.services.document_loader import DocumentLoader

docs = DocumentLoader.load_documents(
    "../data/documents"
)

print(docs)