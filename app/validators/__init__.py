"""
response_validator.py

Responsabilidad:
    Validar la respuesta generada por el agente
    antes de enviarla a la interfaz.
"""

from __future__ import annotations

import logging

from app.schemas.query_response import QueryResponse

logger = logging.getLogger(__name__)

FALLBACK_MESSAGE = (
    "No encontré información en los documentos disponibles."
)


def validar_respuesta(
    respuesta: str,
) -> QueryResponse:
    """
    Valida la respuesta generada por el agente.

    Args:
        respuesta:
            Respuesta generada por el agente.

    Returns:
        QueryResponse validado.
    """

    respuesta = respuesta.strip()

    # Caso 1:
    # El agente no encontró información.

    if FALLBACK_MESSAGE in respuesta:

        logger.warning(
            "El agente no encontró información."
        )

        return QueryResponse(
            answer=FALLBACK_MESSAGE,
            success=False,
        )

    # Caso 2:
    # El agente respondió pero olvidó citar fuentes.

    if "Fuentes:" not in respuesta:

        logger.warning(
            "La respuesta no contiene fuentes."
        )

        return QueryResponse(
            answer=FALLBACK_MESSAGE,
            success=False,
        )

    # Caso válido.

    logger.info(
        "Respuesta validada correctamente."
    )

    return QueryResponse(
        answer=respuesta,
        success=True,
    )