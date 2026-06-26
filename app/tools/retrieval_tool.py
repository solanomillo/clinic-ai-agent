"""
rag_service.py

Responsabilidad:
    Inicializar el agente RAG y ensamblar
    todos los componentes del sistema.
"""

from __future__ import annotations

import logging

from app.agents.rag_agent import (
    crear_rag_agent,
)
from app.models.gemini import (
    cargar_llm,
)
from app.services.vectorstore_service import (
    inicializar_vectorstore,
)
from app.tools.retrieval_tool import (
    crear_retrieval_tool,
)

logger = logging.getLogger(__name__)


def inicializar_rag():
    """
    Inicializa todos los componentes del
    sistema RAG.

    Returns:
        Agente completamente configurado.
    """

    logger.info(
        "Inicializando sistema RAG..."
    )

    # --------------------------------------------------
    # Vector Store
    # --------------------------------------------------

    vectorstore = inicializar_vectorstore()

    # --------------------------------------------------
    # Tool de recuperación
    # --------------------------------------------------

    retrieval_tool = crear_retrieval_tool(
        vectorstore
    )

    # --------------------------------------------------
    # Modelo LLM
    # --------------------------------------------------

    llm = cargar_llm()

    # --------------------------------------------------
    # Agente
    # --------------------------------------------------

    agent = crear_rag_agent(
        llm=llm,
        retrieval_tool=retrieval_tool,
    )

    logger.info(
        "Sistema RAG inicializado correctamente."
    )

    return agent