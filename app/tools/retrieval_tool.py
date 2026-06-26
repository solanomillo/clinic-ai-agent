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
        
        MIN_DOCUMENTS = 2

        if len(documentos) < MIN_DOCUMENTS:

            logger.warning(
                "Contexto insuficiente para responder."
            )

            return (
                "No se encontró suficiente "
                "información en los documentos."
            )

        if not documentos:
            return (
                "No se encontró información "
                "en los documentos."
            )

        contexto = []
        fuentes = []

        for doc in documentos:

            source = doc.metadata.get(
                "document_name",
                "desconocido"
            )

            page = doc.metadata.get(
                "page",
                "N/A"
            )

            fuentes.append(
                f"{source} (Página {page})"
            )

            contexto.append(
                f"""
        Documento: {source}
        Página: {page}

        Contenido:
        {doc.page_content}
        """
            )

        return f"""
        CONTEXTO:

        {chr(10).join(contexto)}

        FUENTES:

        {chr(10).join(set(fuentes))}
        """

    return buscar_documentacion