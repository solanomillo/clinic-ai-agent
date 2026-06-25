"""
pdf_loader.py

Responsabilidad:
    Cargar documentos PDF.
"""

import logging

from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader
)

from langchain_core.documents import (
    Document
)

from app.config.settings import (
    settings
)

logger = logging.getLogger(__name__)


def cargar_documentos() -> list[Document]:
    """
    Carga todos los PDFs disponibles.

    Returns:
        Lista de documentos.
    """

    loader = DirectoryLoader(
        settings.DOCUMENTS_PATH,
        glob="*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
    )

    documentos = loader.load()

    logger.info(
        "Documentos cargados: %s",
        len(documentos)
    )

    return documentos