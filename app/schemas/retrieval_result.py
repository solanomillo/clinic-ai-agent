"""
retrieval_result.py

Representa el resultado de una búsqueda semántica.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from langchain_core.documents import Document


@dataclass(slots=True)
class RetrievalResult:
    """
    Resultado de la búsqueda semántica.
    """

    documents: list[Document]

    confidence: float

    sources: list[str] = field(default_factory=list)