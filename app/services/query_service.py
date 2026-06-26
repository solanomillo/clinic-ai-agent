"""
query_service.py

Responsabilidad:
    Ejecutar consultas contra el pipeline RAG.

Incluye:
    - Retry automático.
    - Manejo de errores.
    - Rate Limit.
    - Logging.
"""

import logging
import time

from app.config.settings import settings

from app.core.exceptions import (
    LLMError,
    RateLimitError
)

logger = logging.getLogger(__name__)


def ejecutar_consulta(
    rag_chain,
    pregunta: str
) -> str:
    """
    Ejecuta una consulta utilizando
    el pipeline RAG.

    Args:
        rag_chain:
            Cadena principal RAG.

        pregunta:
            Consulta del usuario.

    Returns:
        str
    """

    ultimo_error = None

    for intento in range(
        1,
        settings.MAX_RETRIES + 1
    ):

        try:

            logger.info(
                "Consulta recibida: %s",
                pregunta
            )

            respuesta = rag_chain.invoke(
                pregunta
            )

            logger.info(
                "Consulta completada."
            )

            return respuesta

        except Exception as error:

            ultimo_error = error

            mensaje = str(error).lower()

            logger.exception(
                "Error durante consulta."
            )

            # ---------------------------------
            # Rate Limit
            # ---------------------------------

            if (
                "429" in mensaje
                or
                "resource_exhausted"
                in mensaje
                or
                "rate limit"
                in mensaje
            ):
                raise RateLimitError(
                    "Límite de uso alcanzado."
                ) from error

            # ---------------------------------
            # Retry
            # ---------------------------------

            if intento < settings.MAX_RETRIES:

                logger.warning(
                    "Reintentando (%s/%s)...",
                    intento,
                    settings.MAX_RETRIES
                )

                time.sleep(
                    settings.RETRY_DELAY_SECONDS
                )

    raise LLMError(
        "No fue posible completar la consulta."
    ) from ultimo_error