"""
chat.py

Responsabilidad:
    Gestionar la interacción entre el usuario
    y el agente RAG.
"""

from __future__ import annotations

import logging

import streamlit as st

from app.core.exceptions import (
    RateLimitError,
)

from app.ui.session import (
    obtener_agente,
    obtener_historial,
    agregar_mensaje,
)

logger = logging.getLogger(__name__)


def mostrar_historial() -> None:
    """
    Renderiza el historial de conversación.
    """

    for mensaje in obtener_historial():

        with st.chat_message(
            mensaje["role"]
        ):
            st.markdown(
                mensaje["content"]
            )


def procesar_consulta(
    consulta: str
) -> None:
    """
    Envía la consulta al agente y
    muestra la respuesta.
    """

    agregar_mensaje(
        "user",
        consulta
    )

    with st.chat_message("user"):
        st.markdown(consulta)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        try:

            with st.spinner(
                "Consultando documentos..."
            ):

                agent = obtener_agente()

                respuesta = agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": consulta,
                            }
                        ]
                    }
                )

                contenido = (
                    respuesta["messages"][-1].content
                )

                placeholder.markdown(
                    contenido
                )

                agregar_mensaje(
                    "assistant",
                    contenido
                )

        except RateLimitError:

            mensaje = (
                "⚠️ Se alcanzó el límite de solicitudes del modelo. "
                "Intenta nuevamente en unos minutos."
            )

            placeholder.warning(
                mensaje
            )

            agregar_mensaje(
                "assistant",
                mensaje
            )

        except Exception:

            logger.exception(
                "Error procesando consulta."
            )

            mensaje = (
                "❌ Ocurrió un error inesperado. "
                "Por favor intenta nuevamente."
            )

            placeholder.error(
                mensaje
            )

            agregar_mensaje(
                "assistant",
                mensaje
            )


def render_chat() -> None:
    """
    Renderiza el chat completo.
    """

    mostrar_historial()

    consulta = st.chat_input(
        "Escribe tu pregunta..."
    )

    if consulta:

        procesar_consulta(
            consulta
        )