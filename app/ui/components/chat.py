# app/ui/components/chat.py
import streamlit as st
import time
import logging
from app.services.query_service import ejecutar_consulta
from app.core.exceptions import RateLimitError, LLMError

logger = logging.getLogger(__name__)

def display_chat_history():
    """Muestra el historial de mensajes del chat"""
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "user":
                st.markdown(
                    f'<div class="user-message">{message["content"]}</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="assistant-message">{message["content"]}</div>',
                    unsafe_allow_html=True
                )
                
                # Botones de feedback
                if "feedback" not in message:
                    col1, col2, col3 = st.columns([0.1, 0.1, 0.8])
                    with col1:
                        if st.button("👍", key=f"like_{hash(message['content'])}"):
                            st.session_state.feedback_given[hash(message['content'])] = "positive"
                            st.rerun()
                    with col2:
                        if st.button("👎", key=f"dislike_{hash(message['content'])}"):
                            st.session_state.feedback_given[hash(message['content'])] = "negative"
                            st.rerun()
                    with col3:
                        if hash(message['content']) in st.session_state.feedback_given:
                            feedback = st.session_state.feedback_given[hash(message['content'])]
                            st.caption(f"✅ Feedback: {'Positivo' if feedback == 'positive' else 'Negativo'}")

def handle_user_input(rag_chain):
    """Maneja la entrada del usuario y genera respuestas"""
    
    pregunta = st.chat_input(
        "💬 Escribe tu consulta médica aquí...",
        key="chat_input"
    )
    
    if pregunta:
        logger.info(f"Nueva consulta recibida: {pregunta[:50]}...")
        
        # Agregar pregunta al historial
        st.session_state.messages.append({"role": "user", "content": pregunta})
        st.session_state.total_questions += 1
        
        # Mostrar mensaje del usuario
        with st.chat_message("user"):
            st.markdown(
                f'<div class="user-message">{pregunta}</div>',
                unsafe_allow_html=True
            )
        
        # Obtener respuesta
        with st.chat_message("assistant"):
            with st.spinner("🔍 Buscando en la base de conocimiento médico..."):
                time.sleep(0.5)
                
                try:
                    respuesta = ejecutar_consulta(rag_chain, pregunta)
                    
                    st.markdown(
                        f'<div class="assistant-message">{respuesta}</div>',
                        unsafe_allow_html=True
                    )
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": respuesta,
                        "feedback": False
                    })
                    logger.info("Respuesta generada exitosamente")
                    
                except RateLimitError:
                    st.warning("""
                        ⚠️ El servicio de IA alcanzó temporalmente su límite de uso.
                        Intenta nuevamente en unos minutos.
                    """)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "⚠️ El servicio está temporalmente saturado. Por favor, intenta de nuevo en unos minutos.",
                        "feedback": False
                    })
                    
                except LLMError:
                    st.error("""
                        ❌ Ocurrió un problema al procesar tu consulta médica.
                    """)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "❌ Error al procesar la consulta. Por favor, intenta de nuevo.",
                        "feedback": False
                    })
                    
                except Exception as e:
                    logger.error(f"Error inesperado: {str(e)}", exc_info=True)
                    st.error("""
                        ❌ Error inesperado en el sistema.
                    """)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "❌ Error inesperado. Por favor, contacta al soporte técnico.",
                        "feedback": False
                    })
        
        st.rerun()