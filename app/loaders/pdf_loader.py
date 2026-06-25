"""
pdf_loader.py

Responsabilidad:
    Cargar documentos PDF.

Soporta:

- PDFs digitales
- PDFs escaneados mediante OCR
"""

from __future__ import annotations

import logging
from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_core.documents import (
    Document
)

from app.config.settings import (
    settings
)

from app.loaders.ocr_loader import (
    extraer_texto_ocr
)

logger = logging.getLogger(__name__)


def es_pdf_con_texto(
    documentos: list[Document]
) -> bool:
    """
    Determina si el PDF contiene
    texto extraíble.
    """

    texto_total = "".join(
        doc.page_content
        for doc in documentos
    )

    return (
        len(texto_total.strip()) > 100
    )


def cargar_documentos() -> list[Document]:
    """
    Carga todos los PDFs disponibles.

    Detecta automáticamente
    PDFs escaneados.
    """

    documentos_totales = []

    carpeta = Path(
        settings.DOCUMENTS_PATH
    )

    pdfs = list(
        carpeta.glob("*.pdf")
    )

    logger.info(
        "PDFs encontrados: %s",
        len(pdfs)
    )

    for pdf_path in pdfs:

        try:

            logger.info(
                "Procesando: %s",
                pdf_path.name
            )

            loader = PyPDFLoader(
                str(pdf_path)
            )

            documentos = loader.load()

            if es_pdf_con_texto(
                documentos
            ):

                logger.info(
                    "PDF digital detectado: %s",
                    pdf_path.name
                )

                documentos_totales.extend(
                    documentos
                )

            else:

                logger.warning(
                    "PDF escaneado detectado: %s",
                    pdf_path.name
                )

                documentos_ocr = (
                    extraer_texto_ocr(
                        str(pdf_path)
                    )
                )

                documentos_totales.extend(
                    documentos_ocr
                )

        except Exception:

            logger.exception(
                "Error procesando %s",
                pdf_path.name
            )

    logger.info(
        "Total de documentos cargados: %s",
        len(documentos_totales)
    )

    return documentos_totales