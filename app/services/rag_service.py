"""
rag_service.py

Responsabilidad:
    Inicializar el agente RAG.
"""

import logging

from app.services.vectorstore_service import (
    inicializar_vectorstore
)

from app.retrievers.retriever import (
    crear_retriever
)

from app.models.gemini import (
    cargar_llm
)

from app.tools.retrieval_tool import (
    crear_retrieval_tool
)

from app.agents.rag_agent import (
    crear_rag_agent
)

logger = logging.getLogger(__name__)


def inicializar_rag():
    """
    Inicializa el agente RAG completo.
    """

    logger.info(
        "Inicializando Agentic RAG."
    )

    vectorstore = (
        inicializar_vectorstore()
    )

    retriever = crear_retriever(
        vectorstore
    )

    retrieval_tool = (
        crear_retrieval_tool(
            retriever
        )
    )

    llm = cargar_llm()

    agent = crear_rag_agent(
        llm=llm,
        retrieval_tool=retrieval_tool
    )

    logger.info(
        "Agentic RAG inicializado correctamente."
    )

    return agent