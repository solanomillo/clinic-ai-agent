"""
semantic_search_service.py

Responsabilidad:
    Ejecutar la búsqueda semántica sobre el
    vector store y construir el contexto que
    utilizará el agente.
"""

from __future__ import annotations

import logging

from app.config.settings import settings
from app.schemas.retrieval_result import RetrievalResult

logger = logging.getLogger(__name__)


def buscar_contexto(
    vectorstore,
    consulta: str,
) -> RetrievalResult:
    """
    Ejecuta una búsqueda semántica utilizando
    similarity_search_with_score().

    Args:
        vectorstore:
            Índice vectorial FAISS.

        consulta:
            Pregunta realizada por el usuario.

    Returns:
        RetrievalResult con el contexto encontrado.
    """

    logger.info(
        "Iniciando búsqueda semántica."
    )

    resultados = vectorstore.similarity_search_with_score(
        query=consulta,
        k=settings.SEMANTIC_SEARCH_K,
    )

    if not resultados:

        logger.warning(
            "No se recuperaron documentos."
        )

        return RetrievalResult(
            documents=[],
            context="",
            confidence=0.0,
            sources=[],
        )

    documentos = []
    fuentes = []

    mejor_distancia = resultados[0][1]

    for documento, distancia in resultados:

        logger.info(
            "Documento=%s Distancia=%.4f",
            documento.metadata.get(
                "document_name",
                "desconocido",
            ),
            distancia,
        )

        if distancia > settings.SEMANTIC_SCORE_THRESHOLD:
            continue

        documentos.append(documento)

        fuentes.append(
            f"{documento.metadata.get('document_name', 'desconocido')} "
            f"(Página {documento.metadata.get('page', 'N/A')})"
        )

    if not documentos:

        logger.warning(
            "Todos los documentos fueron descartados."
        )

        return RetrievalResult(
            documents=[],
            context="",
            confidence=0.0,
            sources=[],
        )

    contexto = "\n\n".join(
        (
            f"Documento: {doc.metadata.get('document_name', 'desconocido')}\n"
            f"Página: {doc.metadata.get('page', 'N/A')}\n\n"
            f"{doc.page_content}"
        )
        for doc in documentos
    )

    confianza = max(
        0.0,
        1 - mejor_distancia,
    )

    logger.info(
        "Confianza calculada: %.2f",
        confianza,
    )

    return RetrievalResult(
        documents=documentos,
        context=contexto,
        confidence=confianza,
        sources=sorted(set(fuentes)),
    )