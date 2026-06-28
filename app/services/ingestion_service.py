"""
ingestion_service.py

Responsabilidad:
    Orquestar el pipeline de ingesta de documentos para la
    construcción del índice vectorial.

Pipeline:
    1. Cargar documentos.
    2. Limpiar documentos.
    3. Generar chunks.
    4. Cargar embeddings.
    5. Crear VectorStore FAISS.
    6. Guardar el índice en disco.
"""

import logging

from app.loaders.pdf_loader import (
    cargar_documentos,
)
from app.processing.chunking import (
    crear_chunks,
)
from app.processing.cleaning import (
    limpiar_documentos,
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

    logger.info("Starting document ingestion pipeline.")

    documentos = cargar_documentos()

    logger.info("Cleaning loaded documents.")

    documentos = limpiar_documentos(
        documentos
    )

    logger.info("Generating document chunks.")

    chunks = crear_chunks(
        documentos
    )

    logger.info("Loading embedding model.")

    embeddings = cargar_embeddings()

    logger.info("Creating FAISS vector store.")

    vectorstore = crear_vectorstore(
        chunks,
        embeddings,
    )

    guardar_vectorstore(
        vectorstore,
    )

    logger.info("FAISS vector store created successfully.")

    return vectorstore