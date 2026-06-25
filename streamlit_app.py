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
from app.services.query_service import (  # <-- NUEVO IMPORT
    ejecutar_consulta
)
from app.core.exceptions import (  # <-- NUEVO IMPORT
    RateLimitError,
    LLMError
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
st.markdown("""
<style>
    /* Estilo general */
    .main {
        padding: 2rem;
    }
    
    /* Estilo para el título */
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    /* Estilo para mensajes del usuario */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        max-width: 80%;
        margin-left: auto;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Estilo para mensajes del asistente */
    .assistant-message {
        background: #f8f9fa;
        color: #2c3e50;
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        max-width: 80%;
        border-left: 4px solid #667eea;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Estilo para el input */
    .stTextInput > div > div > input {
        border-radius: 25px !important;
        border: 2px solid #e0e0e0;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
    }
    
    /* Estilo para el spinner */
    .stSpinner > div {
        border-color: #667eea transparent transparent transparent !important;
    }
    
    /* Estilo para la barra lateral */
    .sidebar-content {
        padding: 1.5rem 1rem;
    }
    
    .sidebar-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
    }
    
    /* Estadísticas */
    .stat-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
    
    /* Botón de limpiar */
    .clear-btn {
        background: #e74c3c;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .clear-btn:hover {
        background: #c0392b;
        transform: scale(0.98);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #95a5a6;
        padding: 2rem 0 1rem 0;
        border-top: 1px solid #ecf0f1;
        margin-top: 2rem;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

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
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    
    # Logo o título de la app
    st.markdown("## 🤖 RAG Assistant")
    st.markdown("---")
    
    # Información del sistema
    st.markdown("### ℹ️ Información del Sistema")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div>📊 Estado</div>
            <div class="stat-number">🟢</div>
            <div style="font-size: 0.8rem; color: #27ae60;">Activo</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div>❓ Preguntas</div>
            <div class="stat-number">{st.session_state.total_questions}</div>
            <div style="font-size: 0.8rem; color: #7f8c8d;">Totales</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")    
    
    # Opciones de chat
    st.markdown("### 💬 Opciones de Chat")    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧹 Limpiar Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        if st.button("💾 Guardar", use_container_width=True):
            st.info("Chat guardado exitosamente!")    
    st.markdown("---")
    
    # Feedbacks
    st.markdown("### 📊 Estadísticas")
    if st.session_state.total_questions > 0:
        st.metric(
            label="Tasa de respuesta",
            value=f"{(st.session_state.total_questions / max(1, st.session_state.total_questions)):.0%}"
        )
        
        # Gráfico simple de actividad
        st.progress(
            min(1.0, st.session_state.total_questions / 10),
            text=f"Actividad: {min(100, st.session_state.total_questions * 10)}%"
        )
    
    st.markdown("---")
    
    # Footer de la barra lateral
    st.markdown(f"""
    <div style="text-align: center; color: #95a5a6; font-size: 0.8rem; margin-top: 1rem;">
        <div>🔄 Última actualización</div>
        <div style="font-size: 0.7rem;">{datetime.now().strftime('%H:%M:%S')}</div>
        <div style="font-size: 0.7rem; margin-top: 0.5rem;">v1.0.0</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Área principal
st.markdown('<div class="main">', unsafe_allow_html=True)

# Título
st.markdown('<h1 class="main-title">🚀 RAG Avanzado con Langchain</h1>', unsafe_allow_html=True)

# Subtítulo y descripción
st.markdown("""
<div style="background: #f8f9fa; padding: 1rem 1.5rem; border-radius: 10px; margin-bottom: 2rem; border-left: 4px solid #667eea;">
    <p style="margin: 0; color: #2c3e50;">
        💡 <strong>Asistente inteligente</strong> que utiliza RAG (Retrieval-Augmented Generation) 
        para responder consultas con información contextual precisa.
    </p>
</div>
""", unsafe_allow_html=True)

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
                # <-- CÓDIGO MODIFICADO: Usando ejecutar_consulta en lugar de rag_chain.invoke directamente
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
                
            except RateLimitError:  # <-- EXCEPCIÓN ESPECÍFICA
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
                
            except LLMError:  # <-- EXCEPCIÓN ESPECÍFICA
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
                
            except Exception as e:  # <-- EXCEPCIÓN GENÉRICA (catch-all)
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
st.markdown("""
<div class="footer">
    <div style="display: flex; justify-content: center; gap: 2rem; align-items: center;">
        <span>🤖 Powered by Langchain</span>
        <span>•</span>
        <span>📚 RAG Architecture</span>
        <span>•</span>
        <span>🛡️ Advanced Retrieval</span>
    </div>
    <div style="margin-top: 0.5rem;">
        <span>Made with ❤️ para preguntas inteligentes</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)