"""
metadata.py

Responsabilidad:
    Enriquecer los documentos con metadatos que permitan
    trazabilidad, filtrado y citación de fuentes.
"""

from __future__ import annotations

from datetime import datetime, UTC
from pathlib import Path
import uuid

from langchain_core.documents import Document


def enriquecer_metadata(
    documentos: list[Document],
) -> list[Document]:
    """
    Enriquece los metadatos de cada documento.

    Args:
        documentos: Lista de documentos.

    Returns:
        Lista de documentos con metadatos enriquecidos.
    """

    fecha_indexacion = datetime.now(
        UTC
    ).isoformat()

    documentos_enriquecidos: list[Document] = []

    for documento in documentos:

        metadata = documento.metadata.copy()

        source = metadata.get(
            "source",
            ""
        )

        ruta = Path(source)

        filename = ruta.name

        category = (
            ruta.parent.name.lower()
            if ruta.parent.name
            else "general"
        )

        title = (
            ruta.stem
            .replace("_", " ")
            .title()
        )

        document_id = str(
            uuid.uuid5(
                uuid.NAMESPACE_URL,
                f"{category}/{filename}"
            )
        )

        metadata.update(
            {
                "document_id": document_id,
                "category": category,
                "title": title,
                "filename": filename,
                "indexed_at": fecha_indexacion,
            }
        )

        documentos_enriquecidos.append(
            Document(
                page_content=documento.page_content,
                metadata=metadata,
            )
        )

    return documentos_enriquecidos