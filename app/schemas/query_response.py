"""
query_response.py

Responsabilidad:
    Definir el esquema de respuesta utilizado
    entre los servicios y la interfaz.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class QueryResponse:
    """
    Representa la respuesta generada por el agente.

    Attributes:
        answer:
            Respuesta generada por el LLM.

        sources:
            Lista de fuentes utilizadas para responder.

        confidence:
            Nivel de confianza de la búsqueda semántica.

        success:
            Indica si la consulta pudo responderse
            correctamente.
    """

    answer: str

    sources: list[str] = field(default_factory=list)

    confidence: float | None = None

    success: bool = True