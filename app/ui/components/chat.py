"""
chat.py

Responsabilidad:
    Manejar la interacción del chat entre el usuario
    y el sistema RAG.
"""

import streamlit as st
import time
import logging

from app.services.query_service import ejecutar_consulta
from app.core.exceptions import RateLimitError, LLMError

logger = logging.getLogger(__name__)


def display_chat_history():
    """Muestra el historial del chat."""

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            if message["role"] == "user":

                st.markdown(
                    f'<div class="user-message">{message["content"]}</div>',
                    unsafe_allow_html=True,
                )

            else:

                st.markdown(
                    f'<div class="assistant-message">{message["content"]}</div>',
                    unsafe_allow_html=True,
                )

                # Mostrar fuentes si existen
                if "sources" in message and message["sources"]:

                    with st.expander("📌 Fuentes utilizadas"):

                        for src in message["sources"]:

                            st.markdown(
                                f"""
                                **{src.get('title', 'Sin título')}**

                                - Categoría: {src.get('category')}
                                - Archivo: {src.get('filename')}
                                - Página: {src.get('page')}
                                """
                            )

                # Feedback UI
                if "feedback" not in message:

                    col1, col2, col3 = st.columns([0.1, 0.1, 0.8])

                    with col1:

                        if st.button(
                            "👍",
                            key=f"like_{hash(message['content'])}",
                        ):
                            st.session_state.feedback_given[
                                hash(message["content"])
                            ] = "positive"
                            st.rerun()

                    with col2:

                        if st.button(
                            "👎",
                            key=f"dislike_{hash(message['content'])}",
                        ):
                            st.session_state.feedback_given[
                                hash(message["content"])
                            ] = "negative"
                            st.rerun()

                    with col3:

                        if hash(message["content"]) in st.session_state.feedback_given:

                            feedback = st.session_state.feedback_given[
                                hash(message["content"])
                            ]

                            st.caption(
                                f"✅ Feedback: {'Positivo' if feedback == 'positive' else 'Negativo'}"
                            )


def handle_user_input(rag_chain):
    """Maneja la entrada del usuario y genera respuestas."""

    pregunta = st.chat_input(
        "💬 Escribe tu consulta aquí...",
        key="chat_input",
    )

    if pregunta:

        logger.info(
            "Nueva consulta recibida: %s",
            pregunta[:50],
        )

        # Guardar mensaje usuario
        st.session_state.messages.append(
            {"role": "user", "content": pregunta}
        )

        st.session_state.total_questions += 1

        with st.chat_message("user"):

            st.markdown(
                f'<div class="user-message">{pregunta}</div>',
                unsafe_allow_html=True,
            )

        # -----------------------------
        # RESPUESTA RAG
        # -----------------------------
        with st.chat_message("assistant"):

            with st.spinner("🔍 Buscando información..."):

                time.sleep(0.3)

                try:

                    result = ejecutar_consulta(
                        rag_chain,
                        pregunta,
                    )

                    answer = result["answer"]
                    sources = result["sources"]

                    st.markdown(
                        f'<div class="assistant-message">{answer}</div>',
                        unsafe_allow_html=True,
                    )

                    # Mostrar fuentes en UI
                    if sources:

                        with st.expander("📌 Fuentes utilizadas"):

                            for src in sources:

                                st.markdown(
                                    f"""
                                    **{src.get('title', 'Sin título')}**

                                    - Categoría: {src.get('category')}
                                    - Archivo: {src.get('filename')}
                                    - Página: {src.get('page')}
                                    """
                                )

                    # Guardar en historial
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "sources": sources,
                            "feedback": False,
                        }
                    )

                    logger.info("Respuesta generada correctamente.")

                except RateLimitError:

                    st.warning(
                        "⚠️ Límite de uso alcanzado. Intenta más tarde."
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": "⚠️ Servicio saturado.",
                            "sources": [],
                            "feedback": False,
                        }
                    )

                except LLMError:

                    st.error(
                        "❌ Error al procesar la consulta."
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": "❌ Error en el modelo.",
                            "sources": [],
                            "feedback": False,
                        }
                    )

                except Exception as e:

                    logger.error(
                        "Error inesperado: %s",
                        str(e),
                        exc_info=True,
                    )

                    st.error(
                        "❌ Error inesperado en el sistema."
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": "❌ Error interno.",
                            "sources": [],
                            "feedback": False,
                        }
                    )

        st.rerun()