from pathlib import Path
from pypdf import PdfReader
from docx import Document


class DocumentLoader:

    @staticmethod
    def load_documents(folder_path: str):

        documents = []

        folder = Path(folder_path)

        for file in folder.iterdir():

            if file.suffix == ".txt":

                content = file.read_text(
                    encoding="utf-8"
                )

            elif file.suffix == ".pdf":

                reader = PdfReader(file)

                content = ""

                for page in reader.pages:
                    content += page.extract_text()

            elif file.suffix == ".docx":

                doc = Document(file)

                content = "\n".join(
                    para.text
                    for para in doc.paragraphs
                )

            else:
                continue

            documents.append(
                {
                    "filename": file.name,
                    "content": content
                }
            )

        return documents