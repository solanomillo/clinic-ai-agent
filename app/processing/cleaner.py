"""
cleaner.py

Responsabilidad:
    Limpiar y normalizar documentos
    antes del chunking.
"""

import re
import logging

from langchain_core.documents import (
    Document
)

logger = logging.getLogger(__name__)


def limpiar_documentos(
    documentos: list[Document]
) -> list[Document]:
    """
    Limpia el contenido textual
    preservando los metadatos.

    Args:
        documentos:
            Lista de documentos LangChain.

    Returns:
        Lista de documentos limpios.
    """

    documentos_limpios = []

    for documento in documentos:

        texto = documento.page_content

        # Espacios duplicados
        texto = re.sub(
            r"\s+",
            " ",
            texto
        )

        # Saltos de línea excesivos
        texto = re.sub(
            r"\n+",
            "\n",
            texto
        )

        # Limpieza final
        texto = texto.strip()

        documentos_limpios.append(
            Document(
                page_content=texto,
                metadata=documento.metadata
            )
        )

    logger.info(
        "Documentos limpiados: %s",
        len(documentos_limpios)
    )

    return documentos_limpios