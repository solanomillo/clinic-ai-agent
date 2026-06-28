"""
vectorstore_service.py

Responsabilidad:
    Administrar la inicialización del índice vectorial.

    Si el índice FAISS existe, se carga desde disco.
    En caso contrario, se delega la construcción del índice
    al servicio de ingesta.
"""

import logging

from app.processing.embeddings import (
    cargar_embeddings,
)
from app.services.ingestion_service import (
    construir_vectorstore,
)
from app.vectorstores.faiss_store import (
    cargar_vectorstore,
    existe_vectorstore,
)

logger = logging.getLogger(__name__)


def inicializar_vectorstore():
    """
    Inicializa el VectorStore.

    Returns:
        FAISS: Instancia lista para realizar búsquedas semánticas.
    """

    embeddings = cargar_embeddings()

    if existe_vectorstore():

        logger.info(
            "Cargando índice FAISS existente."
        )

        return cargar_vectorstore(
            embeddings
        )

    logger.info(
        "No existe un índice FAISS. Se iniciará la construcción."
    )

    return construir_vectorstore()