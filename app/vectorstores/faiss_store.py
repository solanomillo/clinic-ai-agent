"""
faiss_store.py

Responsabilidad:
    Gestionar la creación, persistencia
    y carga del índice vectorial FAISS.
"""

from __future__ import annotations

import logging
from pathlib import Path

from langchain_community.vectorstores import (
    FAISS
)

from app.config.settings import (
    settings
)

from app.core.exceptions import (
    VectorStoreError
)

logger = logging.getLogger(__name__)


def crear_vectorstore(
    chunks,
    embeddings
) -> FAISS:
    """
    Crea un índice FAISS a partir
    de los chunks generados.

    Args:
        chunks:
            Fragmentos de documentos.

        embeddings:
            Modelo de embeddings.

    Returns:
        FAISS
    """

    try:

        logger.info(
            "Creando índice FAISS con %s chunks.",
            len(chunks)
        )

        vectorstore = FAISS.from_documents(
            chunks,
            embeddings
        )

        logger.info(
            "Índice FAISS creado correctamente."
        )

        return vectorstore

    except Exception as error:

        logger.exception(
            "Error al crear FAISS."
        )

        raise VectorStoreError(
            "No fue posible crear el índice FAISS."
        ) from error


def guardar_vectorstore(
    vectorstore: FAISS
) -> None:
    """
    Guarda el índice FAISS en disco.
    """

    try:

        logger.info(
            "Guardando índice FAISS en %s",
            settings.VECTOR_DB_PATH
        )

        vectorstore.save_local(
            settings.VECTOR_DB_PATH
        )

        logger.info(
            "Índice FAISS guardado correctamente."
        )

    except Exception as error:

        logger.exception(
            "Error al guardar FAISS."
        )

        raise VectorStoreError(
            "No fue posible guardar el índice FAISS."
        ) from error


def cargar_vectorstore(
    embeddings
) -> FAISS:
    """
    Carga un índice FAISS existente.

    Returns:
        FAISS
    """

    try:

        logger.info(
            "Cargando índice FAISS..."
        )

        vectorstore = FAISS.load_local(
            settings.VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        logger.info(
            "Índice FAISS cargado correctamente."
        )

        return vectorstore

    except Exception as error:

        logger.exception(
            "Error al cargar FAISS."
        )

        raise VectorStoreError(
            "No fue posible cargar el índice FAISS."
        ) from error


def existe_vectorstore() -> bool:
    """
    Verifica si existe un índice FAISS.

    Returns:
        bool
    """

    ruta = Path(
        settings.VECTOR_DB_PATH
    )

    existe = ruta.exists()

    logger.info(
        "FAISS existe: %s",
        existe
    )

    return existe