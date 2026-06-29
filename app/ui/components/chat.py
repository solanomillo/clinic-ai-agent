"""
chat.py

Responsabilidad:
    Manejar la interacción del chat entre el usuario
    y el sistema RAG.
"""

import streamlit as st
import time
import logging
import html

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
                # Decodificar el HTML del mensaje del asistente
                content_decoded = html.unescape(message["content"])
                
                st.markdown(
                    f'<div class="assistant-message">{content_decoded}</div>',
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
                message_idx = st.session_state.messages.index(message)
                message_id = f"msg_{message_idx}_{hash(message['content'])}"
                feedback_key = f"feedback_{message_id}"
                
                if feedback_key not in st.session_state:
                    col1, col2, col3 = st.columns([0.1, 0.1, 0.8])

                    with col1:
                        if st.button("👍", key=f"like_{message_id}"):
                            st.session_state[feedback_key] = "positive"
                            st.rerun()

                    with col2:
                        if st.button("👎", key=f"dislike_{message_id}"):
                            st.session_state[feedback_key] = "negative"
                            st.rerun()

                    with col3:
                        pass
                else:
                    feedback = st.session_state[feedback_key]
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

                    # Decodificar el HTML de la respuesta
                    answer_decoded = html.unescape(answer)

                    st.markdown(
                        f'<div class="assistant-message">{answer_decoded}</div>',
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
                            "content": "⚠️ Servicio saturado. Intenta más tarde.",
                            "sources": [],
                        }
                    )

                except LLMError:

                    st.error(
                        "❌ Error al procesar la consulta."
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": "❌ Error en el modelo. Por favor, intenta nuevamente.",
                            "sources": [],
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
                            "content": "❌ Error interno del sistema. Por favor, intenta más tarde.",
                            "sources": [],
                        }
                    )

        st.rerun()