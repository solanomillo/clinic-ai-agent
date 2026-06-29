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
from app.processing.metadata import (
    enriquecer_metadata,
)

logger = logging.getLogger(__name__)


def construir_vectorstore():
    """
    Construye un nuevo índice vectorial FAISS a partir de los
    documentos disponibles y lo almacena en disco.

    Returns:
        FAISS: Instancia del VectorStore creada.
    """

    logger.info("Iniciando el proceso de ingesta de documentos.")

    documentos = cargar_documentos()
    logger.info("Se cargaron %d documentos.", len(documentos))

    documentos = limpiar_documentos(documentos)
    logger.info("Limpieza de documentos completada.")

    documentos = enriquecer_metadata(documentos)
    logger.info("Metadatos enriquecidos correctamente.")

    chunks = crear_chunks(documentos)
    logger.info("Se generaron %d fragmentos (chunks).", len(chunks))

    logger.info("Cargando el modelo de embeddings.")
    embeddings = cargar_embeddings()

    logger.info("Creando el índice vectorial FAISS.")
    vectorstore = crear_vectorstore(chunks, embeddings)

    logger.info("Guardando el índice vectorial en disco.")
    guardar_vectorstore(vectorstore)

    logger.info("Proceso de ingesta finalizado correctamente.")

    return vectorstore