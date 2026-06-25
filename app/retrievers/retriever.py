"""
retriever.py

Responsabilidad:
    Crear el retriever utilizado
    para recuperar contexto desde FAISS.
"""

import logging

from app.config.settings import (
    settings
)

logger = logging.getLogger(__name__)


def crear_retriever(
    vectorstore
):
    """
    Construye un retriever basado
    en FAISS.

    Args:
        vectorstore:
            Índice vectorial FAISS.

    Returns:
        Retriever configurado.
    """

    try:

        logger.info(
            "Creando retriever (%s)",
            settings.RETRIEVER_SEARCH_TYPE
        )

        retriever = (
            vectorstore.as_retriever(
                search_type=
                settings.RETRIEVER_SEARCH_TYPE,

                search_kwargs={
                    "k":
                        settings.RETRIEVER_K,

                    "fetch_k":
                        settings.RETRIEVER_FETCH_K,

                    "lambda_mult":
                        settings.RETRIEVER_LAMBDA_MULT
                }
            )
        )

        logger.info(
            "Retriever creado correctamente."
        )

        return retriever

    except Exception as error:

        logger.exception(
            "Error al crear retriever."
        )

        raise