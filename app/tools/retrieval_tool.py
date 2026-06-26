"""
retrieval_tool.py

Tool encargada de recuperar contexto
desde el vector store.
"""

from __future__ import annotations

import logging

from langchain.tools import tool

from app.services.semantic_search_service import (
    buscar_contexto,
)

logger = logging.getLogger(__name__)


def crear_retrieval_tool(vectorstore):
    """
    Construye la herramienta utilizada por el agente.
    """

    @tool
    def buscar_documentacion(
        consulta: str,
    ) -> str:
        """
        Busca información relevante
        dentro de la base documental.
        """

        resultado = buscar_contexto(
            vectorstore,
            consulta,
        )

        if not resultado.documents:

            return (
                "No encontré información en los documentos disponibles."
            )

        return f"""
        CONTEXTO

        {resultado.context}

        FUENTES

        {chr(10).join(resultado.sources)}
        """

    return buscar_documentacion