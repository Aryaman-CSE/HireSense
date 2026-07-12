from pathlib import Path

import pdfplumber
from docx import Document


class ExtractionService:

    @staticmethod
    def extract_text(file_path: str) -> str:
        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return ExtractionService._extract_pdf(file_path)

        if extension == ".docx":
            return ExtractionService._extract_docx(file_path)

        raise ValueError("Unsupported file type.")

    @staticmethod
    def _extract_pdf(file_path: str) -> str:
        text = ""

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    @staticmethod
    def _extract_docx(file_path: str) -> str:
        document = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )