"""
vectorstore_service.py

Responsabilidad:
    Orquestar la creación o carga
    del índice vectorial FAISS.
"""

from __future__ import annotations

import logging
import time

from app.loaders.pdf_loader import (
    cargar_documentos
)

from app.processing.cleaner import (
    limpiar_documentos
)

from app.processing.chunking import (
    crear_chunks
)

from app.processing.embeddings import (
    cargar_embeddings
)

from app.vectorstores.faiss_store import (
    crear_vectorstore,
    guardar_vectorstore,
    cargar_vectorstore,
    existe_vectorstore
)

from app.core.exceptions import (
    VectorStoreError
)

logger = logging.getLogger(__name__)


def inicializar_vectorstore():
    """
    Inicializa el vector store.

    Flujo:

    1. Cargar embeddings.
    2. Verificar existencia de FAISS.
    3. Cargar FAISS o crearlo.
    """

    inicio = time.time()

    try:

        embeddings = cargar_embeddings()

        if existe_vectorstore():

            logger.info(
                "Cargando índice FAISS existente."
            )

            return cargar_vectorstore(
                embeddings
            )

        logger.info(
            "No existe índice FAISS. Se iniciará la construcción."
        )

        documentos = cargar_documentos()

        if not documentos:

            raise VectorStoreError(
                "No se encontraron documentos para indexar."
            )

        logger.info(
            "Documentos cargados: %s",
            len(documentos)
        )

        documentos = limpiar_documentos(
            documentos
        )

        chunks = crear_chunks(
            documentos
        )

        if not chunks:

            raise VectorStoreError(
                "No se generaron chunks válidos."
            )

        logger.info(
            "Total de chunks generados: %s",
            len(chunks)
        )

        vectorstore = crear_vectorstore(
            chunks,
            embeddings
        )

        guardar_vectorstore(
            vectorstore
        )

        tiempo_total = (
            time.time() - inicio
        )

        logger.info(
            "VectorStore inicializado correctamente en %.2f segundos.",
            tiempo_total
        )

        return vectorstore

    except Exception as error:

        logger.exception(
            "Error durante la inicialización del vector store."
        )

        raise VectorStoreError(
            "No fue posible inicializar el vector store."
        ) from error