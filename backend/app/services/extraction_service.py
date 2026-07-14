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

        raise ValueError("Unsupported file format.")

    @staticmethod
    def _extract_pdf(file_path: str) -> str:
        text = []

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text.append(page_text)

        return "\n".join(text).strip()

    @staticmethod
    def _extract_docx(file_path: str) -> str:
        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text.strip())

        return "\n".join(paragraphs).strip()