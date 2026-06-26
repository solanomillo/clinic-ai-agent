# app/ui/pages/main.py
import streamlit as st
import logging
from app.config.settings import settings
from app.services.rag_service import inicializar_rag
from app.core.logging_config import configurar_logging
from app.config.validator import validar_configuracion
from app.ui.styles.theme import apply_custom_theme
from app.ui.components.sidebar import render_sidebar
from app.ui.components.chat import display_chat_history, handle_user_input
from app.ui.components.footer import render_footer

# Configuración de logging y validación
configurar_logging()
logger = logging.getLogger(__name__)
validar_configuracion()

def main():
    """Página principal de la aplicación"""
    
    # Configuración de la página
    st.set_page_config(
        page_title="Clínica AI - Asistente Médico",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Aplicar tema personalizado
    apply_custom_theme()
    
    # Inicializar estado de sesión
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "total_questions" not in st.session_state:
        st.session_state.total_questions = 0
    if "feedback_given" not in st.session_state:
        st.session_state.feedback_given = {}
    
    # Cargar sistema RAG (caché)
    @st.cache_resource
    def cargar_rag():
        logger.info("Inicializando el sistema RAG...")
        with st.spinner("🔄 Inicializando el sistema médico..."):
            return inicializar_rag()
    
    rag_chain = cargar_rag()
    
    # Renderizar barra lateral
    render_sidebar()
    
    # Área principal
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Título
    st.markdown("""
    <h1 class="main-title">🏥 Clínica AI - Asistente Inteligente</h1>
    <div class="subtitle">Consultas, turnos, coberturas, políticas y más</div>
    """, unsafe_allow_html=True)
    
    # Info box
    st.markdown("""
    <div class="info-box">
        <p>
            💡 <strong>¿Cómo puedo ayudarte?</strong> Este asistente está diseñado para responder 
            consultas sobre <strong>turnos médicos</strong>, <strong>coberturas de salud</strong>, 
            <strong>políticas de cancelación</strong>, <strong>privacidad de datos</strong> y 
            más información sobre nuestra clínica.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mostrar historial de mensajes
    display_chat_history()
    
    # Input del usuario
    st.markdown("---")
    with st.container():
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            handle_user_input(rag_chain)
        with col2:
            st.markdown("""
            <div style="text-align: center; padding-top: 0.5rem;">
                <span style="font-size: 2rem; cursor: help;" title="Presiona Enter para enviar">⏎</span>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    render_footer()
    
    st.markdown('</div>', unsafe_allow_html=True)