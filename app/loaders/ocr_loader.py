"""
ocr_loader.py

Procesamiento de PDFs escaneados.
"""

import logging

from pathlib import Path

import pytesseract

from pdf2image import convert_from_path

from langchain_core.documents import (
    Document
)

from app.config.settings import (
    settings
)

logger = logging.getLogger(__name__)


def extraer_texto_ocr(
    pdf_path: str
) -> list[Document]:
    """
    Extrae texto utilizando OCR.
    """

    logger.info(
        "Iniciando OCR: %s",
        pdf_path
    )

    imagenes = convert_from_path(
        pdf_path
    )

    documentos = []

    for pagina, imagen in enumerate(
        imagenes,
        start=1
    ):

        texto = pytesseract.image_to_string(
            imagen,
            lang=settings.OCR_LANGUAGE
        )

        texto = texto.strip()
        
        documentos.append(
            Document(
                page_content=texto,
                metadata={
                    "source": pdf_path,
                    "page": pagina
                }
            )
        )

    logger.info(
        "OCR completado: %s páginas",
        len(documentos)
    )

    return documentos