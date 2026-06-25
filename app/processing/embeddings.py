"""
embeddings.py

Responsabilidad:
    Crear y configurar el modelo
    de embeddings utilizado por el sistema RAG.
"""

import logging

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from app.config.settings import (
    settings
)

from app.core.exceptions import (
    EmbeddingError
)

logger = logging.getLogger(__name__)


def cargar_embeddings() -> HuggingFaceEmbeddings:
    """
    Inicializa el modelo de embeddings.

    Returns:
        HuggingFaceEmbeddings
    """

    try:

        logger.info(
            "Cargando modelo de embeddings: %s",
            settings.EMBEDDING_MODEL_DOS
        )

        embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL_DOS
        )

        logger.info(
            "Modelo de embeddings cargado correctamente."
        )

        return embeddings

    except Exception as error:

        logger.exception(
            "Error al cargar embeddings."
        )

        raise EmbeddingError(
            "No fue posible inicializar el modelo de embeddings."
        ) from error