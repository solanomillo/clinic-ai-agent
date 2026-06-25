"""
session.py

Responsabilidad:
    Gestionar el estado global de la aplicación Streamlit.
"""

from __future__ import annotations

import logging

import streamlit as st

from app.services.rag_service import (
    inicializar_rag,
)

logger = logging.getLogger(__name__)


def inicializar_sesion() -> None:
    """
    Inicializa las variables necesarias para la aplicación.

    Esta función debe ejecutarse una única vez al iniciar
    la aplicación.
    """

    if "agent" not in st.session_state:

        logger.info(
            "Inicializando agente RAG..."
        )

        st.session_state.agent = (
            inicializar_rag()
        )

    if "messages" not in st.session_state:

        st.session_state.messages = []

    if "processing" not in st.session_state:

        st.session_state.processing = False


def obtener_agente():
    """
    Devuelve la instancia del agente RAG.
    """

    return st.session_state.agent


def obtener_historial() -> list:
    """
    Devuelve el historial de conversación.
    """

    return st.session_state.messages


def agregar_mensaje(
    role: str,
    content: str
) -> None:
    """
    Agrega un mensaje al historial.

    Args:
        role: Rol del mensaje ("user" o "assistant").
        content: Contenido del mensaje.
    """

    st.session_state.messages.append(
        {
            "role": role,
            "content": content
        }
    )


def limpiar_historial() -> None:
    """
    Elimina todos los mensajes del chat.
    """

    logger.info(
        "Limpiando historial de conversación."
    )

    st.session_state.messages = []