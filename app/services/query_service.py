"""
query_service.py

Responsabilidad:
    Ejecutar consultas contra el pipeline RAG
    y construir respuesta + fuentes estructuradas.
"""

import logging
import time

from app.config.settings import settings
from app.core.exceptions import (
    LLMError,
    RateLimitError,
)

logger = logging.getLogger(__name__)


def ejecutar_consulta(
    rag_chain,
    pregunta: str,
) -> dict:
    """
    Ejecuta una consulta al sistema RAG y construye
    respuesta estructurada con fuentes.

    Args:
        rag_chain:
            Cadena RAG.

        pregunta:
            Consulta del usuario.

    Returns:
        dict:
            {
                "answer": str,
                "sources": list[dict]
            }
    """

    ultimo_error = None

    for intento in range(
        1,
        settings.MAX_RETRIES + 1,
    ):

        try:

            logger.info(
                "Nueva consulta recibida: %s",
                pregunta,
            )

            resultado = rag_chain.invoke(pregunta)

            answer = resultado["answer"]
            documents = resultado["documents"]

            sources = []

            for doc in documents:

                metadata = doc.metadata

                sources.append(
                    {
                        "title": metadata.get("title"),
                        "category": metadata.get("category"),
                        "filename": metadata.get("filename"),
                        "page": metadata.get("page"),
                    }
                )

            logger.info(
                "Consulta completada correctamente."
            )

            return {
                "answer": answer,
                "sources": sources,
            }

        except Exception as error:

            ultimo_error = error

            mensaje = str(error).lower()

            logger.exception(
                "Error durante la consulta."
            )

            if (
                "429" in mensaje
                or "resource_exhausted" in mensaje
                or "rate limit" in mensaje
            ):
                raise RateLimitError(
                    "Límite de uso alcanzado."
                ) from error

            if intento < settings.MAX_RETRIES:

                logger.warning(
                    "Reintentando (%s/%s)...",
                    intento,
                    settings.MAX_RETRIES,
                )

                time.sleep(
                    settings.RETRY_DELAY_SECONDS,
                )

    raise LLMError(
        "No fue posible completar la consulta."
    ) from ultimo_error