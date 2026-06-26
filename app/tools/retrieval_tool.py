"""
retrieval_tool.py

Tool encargada de recuperar contexto
desde el vector store.
"""

import logging

from langchain.tools import tool

logger = logging.getLogger(__name__)


def crear_retrieval_tool(retriever):
    """
    Construye una herramienta de recuperación
    para ser utilizada por el agente.
    """

    @tool
    def buscar_documentacion(
        consulta: str
    ) -> str:
        """
        Busca información relevante
        en la base documental.
        """

        logger.info(
            "Buscando contexto para: %s",
            consulta
        )

        documentos = retriever.invoke(
            consulta
        )

        if not documentos:
            return (
                "No se encontró información "
                "en los documentos."
            )

        contexto = []

        for doc in documentos:

            source = doc.metadata.get(
                "document_name",
                "desconocido"
            )

            page = doc.metadata.get(
                "page",
                "N/A"
            )

            contexto.append(
                f"""
Documento: {source}
Página: {page}

Contenido:
{doc.page_content}
"""
            )

        return "\n\n".join(
            contexto
        )

    return buscar_documentacion