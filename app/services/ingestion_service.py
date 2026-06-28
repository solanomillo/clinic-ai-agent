"""
ingestion_service.py

Responsabilidad:
    Orquestar el pipeline de ingesta de documentos para la
    construcción del índice vectorial.

Pipeline:
    1. Cargar documentos.
    2. Generar chunks.
    3. Cargar embeddings.
    4. Crear VectorStore FAISS.
    5. Guardar el índice en disco.
"""

import logging

from app.loaders.pdf_loader import (
    cargar_documentos,
)
from app.processing.chunking import (
    crear_chunks,
)
from app.processing.embeddings import (
    cargar_embeddings,
)
from app.vectorstores.faiss_store import (
    crear_vectorstore,
    guardar_vectorstore,
)

logger = logging.getLogger(__name__)


def construir_vectorstore():
    """
    Construye un nuevo índice vectorial FAISS a partir de los
    documentos disponibles y lo almacena en disco.

    Returns:
        FAISS: Instancia del VectorStore creada.
    """

    logger.info("Iniciando pipeline de ingesta de documentos.")

    documentos = cargar_documentos()

    chunks = crear_chunks(
        documentos
    )

    embeddings = cargar_embeddings()

    vectorstore = crear_vectorstore(
        chunks,
        embeddings
    )

    guardar_vectorstore(
        vectorstore
    )

    logger.info("Índice FAISS creado y almacenado correctamente.")

    return vectorstore