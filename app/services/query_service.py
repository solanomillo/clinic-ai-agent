"""
query_service.py

Responsabilidad:
    Ejecutar consultas al agente RAG y devolver
    una respuesta estructurada para la interfaz.
"""

from __future__ import annotations

import logging
from typing import Any

from app.core.exceptions import (
    RateLimitError,
)

logger = logging.getLogger(__name__)


def ejecutar_consulta(
    agent: Any,
    pregunta: str,
) -> str:
    """
    Ejecuta una consulta sobre el agente.

    Args:
        agent:
            Instancia del agente RAG.

        pregunta:
            Consulta realizada por el usuario.

    Returns:
        Respuesta generada por el agente.

    Raises:
        RateLimitError:
            Cuando el proveedor del modelo alcanza
            el límite de solicitudes.
    """

    logger.info(
        "Procesando consulta: %s",
        pregunta,
    )

    try:

        resultado = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": pregunta,
                    }
                ]
            }
        )

        respuesta = (
            resultado["messages"][-1].content
        )

        logger.info(
            "Consulta procesada correctamente."
        )

        return respuesta

    except Exception as error:

        if "429" in str(error):

            logger.warning(
                "Rate limit alcanzado."
            )

            raise RateLimitError(
                "El proveedor alcanzó el límite de solicitudes."
            ) from error

        logger.exception(
            "Error ejecutando la consulta."
        )

        raise