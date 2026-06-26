"""
retrieval_tool.py

Responsabilidad:
    Recuperar contexto desde el índice vectorial
    utilizando búsqueda semántica con score.
"""

from __future__ import annotations

import logging

from langchain.tools import tool

from app.config.settings import settings

logger = logging.getLogger(__name__)


def crear_retrieval_tool(vectorstore):
    """
    Construye la herramienta utilizada por el agente
    para recuperar información desde FAISS.
    """

    @tool
    def buscar_documentacion(
        consulta: str,
    ) -> str:
        """
        Recupera contexto utilizando búsqueda semántica.
        """

        logger.info(
            "Consulta recibida: %s",
            consulta,
        )

        resultados = (
            vectorstore.similarity_search_with_score(
                query=consulta,
                k=settings.SEMANTIC_SEARCH_K,
            )
        )

        if not resultados:

            logger.warning(
                "No se encontraron documentos."
            )

            return (
                "No encontré información en los documentos disponibles."
            )

        documentos_validos = []
        fuentes = []

        mejor_distancia = resultados[0][1]

        for documento, distancia in resultados:

            logger.info(
                "Documento=%s | Distancia=%.4f",
                documento.metadata.get(
                    "document_name",
                    "desconocido",
                ),
                distancia,
            )

            if distancia > settings.SEMANTIC_SCORE_THRESHOLD:
                continue

            documentos_validos.append(documento)

            fuente = (
                f"{documento.metadata.get('document_name', 'desconocido')} "
                f"(Página {documento.metadata.get('page', 'N/A')})"
            )

            fuentes.append(fuente)

        if not documentos_validos:

            logger.warning(
                "Todos los documentos fueron descartados por el umbral."
            )

            return (
                "No encontré información en los documentos disponibles."
            )

        confianza = max(
            0.0,
            1 - mejor_distancia,
        )

        logger.info(
            "Confianza calculada: %.2f",
            confianza,
        )

        contexto = "\n\n".join(
            [
                (
                    f"Documento: {doc.metadata.get('document_name','desconocido')}\n"
                    f"Página: {doc.metadata.get('page','N/A')}\n\n"
                    f"{doc.page_content}"
                )
                for doc in documentos_validos
            ]
        )

        return (
            f"Confianza: {confianza:.2f}\n\n"
            f"Contexto:\n\n{contexto}\n\n"
            f"Fuentes:\n"
            + "\n".join(sorted(set(fuentes)))
        )

    return buscar_documentacion