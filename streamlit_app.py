import streamlit as st
from datetime import datetime
import time
import logging
from app.config.settings import settings
from app.services.rag_service import (
    inicializar_rag
)
from app.core.logging_config import (
    configurar_logging
)
from app.config.validator import (
    validar_configuracion
)
from app.services.query_service import (
    ejecutar_consulta
)
from app.core.exceptions import (
    RateLimitError,
    LLMError
)
from app.ui.styles import (
    aplicar_estilos,
)
from app.ui.sidebar import (
    render_sidebar,
)
from app.ui.header import (  # <-- NUEVO IMPORT PARA HEADER Y FOOTER
    render_header,
    render_footer,
)

# Configuración de logging y validación
configurar_logging()
logger = logging.getLogger(__name__)
validar_configuracion()

# Configuración de la página
st.set_page_config(
    page_title="RAG Avanzado con Langchain",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la interfaz
aplicar_estilos()

# Inicializar el estado de la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "feedback_given" not in st.session_state:
    st.session_state.feedback_given = {}

@st.cache_resource
def cargar_rag():
    logger.info("Inicializando el sistema RAG...")
    with st.spinner("🔄 Inicializando el sistema RAG..."):
        return inicializar_rag()

# Cargar el sistema RAG
rag_chain = cargar_rag()

# Barra lateral
render_sidebar()

# Header principal
render_header()  # <-- REEMPLAZA EL BLOQUE DE MAIN

# Mostrar historial de mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)
            
            # Botones de feedback para respuestas del asistente
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

# Input del usuario
st.markdown("---")
with st.container():
    col1, col2 = st.columns([0.9, 0.1])
    with col1:
        pregunta = st.chat_input(
            "💬 Escribe tu pregunta aquí...",
            key="chat_input"
        )
    with col2:
        st.markdown("""
        <div style="text-align: center; padding-top: 0.5rem;">
            <span style="font-size: 2rem; cursor: help;" title="Presiona Enter para enviar">⏎</span>
        </div>
        """, unsafe_allow_html=True)

# Procesar la pregunta
if pregunta:
    logger.info(f"Nueva pregunta recibida: {pregunta[:50]}...")
    
    # Agregar pregunta al historial
    st.session_state.messages.append({"role": "user", "content": pregunta})
    st.session_state.total_questions += 1
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(f'<div class="user-message">{pregunta}</div>', unsafe_allow_html=True)
    
    # Obtener respuesta
    with st.chat_message("assistant"):
        with st.spinner("🔍 Consultando la base de conocimiento..."):
            # Simular tiempo de procesamiento
            time.sleep(0.5)
            
            try:
                # Usando ejecutar_consulta en lugar de rag_chain.invoke directamente
                respuesta = ejecutar_consulta(
                    rag_chain,
                    pregunta
                )
                
                st.markdown(
                    f'<div class="assistant-message">{respuesta}</div>',
                    unsafe_allow_html=True
                )
                
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": respuesta,
                        "feedback": False
                    }
                )
                logger.info("Respuesta generada exitosamente")
                
            except RateLimitError:
                st.warning(
                    """
                    ⚠️ El servicio de IA alcanzó
                    temporalmente su límite de uso.
                    
                    Intenta nuevamente en unos minutos.
                    """
                )
                # Guardar mensaje de error en el historial
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": "⚠️ El servicio de IA alcanzó temporalmente su límite de uso. Intenta nuevamente en unos minutos.",
                        "feedback": False
                    }
                )
                
            except LLMError:
                st.error(
                    """
                    ❌ Ocurrió un problema al
                    procesar tu consulta.
                    """
                )
                # Guardar mensaje de error en el historial
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": "❌ Ocurrió un problema al procesar tu consulta. Por favor, intenta de nuevo.",
                        "feedback": False
                    }
                )
                
            except Exception as e:
                logger.error(f"Error inesperado: {str(e)}", exc_info=True)
                st.error(
                    """
                    ❌ Error inesperado.
                    """
                )
                # Guardar mensaje de error en el historial
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": "❌ Error inesperado. Por favor, intenta de nuevo o contacta al soporte.",
                        "feedback": False
                    }
                )
    
    st.rerun()

# Footer
render_footer() 