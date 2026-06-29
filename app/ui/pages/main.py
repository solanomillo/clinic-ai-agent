"""
main.py

Responsabilidad:
    Punto de entrada principal de la interfaz de usuario.

Inicializa la configuración de la aplicación, carga el sistema RAG,
renderiza los componentes de la interfaz y gestiona la interacción
del usuario.
"""

from __future__ import annotations

import logging

import streamlit as st

from app.config.validator import validar_configuracion
from app.core.logging_config import configurar_logging
from app.services.rag_service import inicializar_rag
from app.ui.components.chat import (
    display_chat_history,
    handle_user_input,
)
from app.ui.components.footer import render_footer
from app.ui.components.sidebar import render_sidebar
from app.ui.styles.theme import apply_custom_theme

logger = logging.getLogger(__name__)


@st.cache_resource
def cargar_rag():
    """
    Inicializa el sistema RAG utilizando caché.

    Returns:
        Instancia del sistema RAG.
    """
    logger.info("Inicializando el sistema RAG...")

    with st.spinner("🔄 Inicializando el sistema médico..."):
        return inicializar_rag()


def inicializar_sesion() -> None:
    """
    Inicializa las variables de sesión de Streamlit.
    """
    st.session_state.setdefault("messages", [])
    st.session_state.setdefault("total_questions", 0)
    st.session_state.setdefault("feedback_given", {})


def main() -> None:
    """
    Renderiza la página principal de la aplicación.
    """

    configurar_logging()
    validar_configuracion()

    st.set_page_config(
        page_title="Clínica AI - Asistente Médico",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    apply_custom_theme()

    inicializar_sesion()

    rag_chain = cargar_rag()

    render_sidebar()

    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.markdown(
        """
        <h1 class="main-title">
            🏥 Clínica AI - Asistente Inteligente
        </h1>

        <div class="subtitle">
            Consultas, turnos, coberturas, políticas y más
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========== INFO-BOX CON st.html() ==========
    st.html(
        """
        <div class="info-box">
            <p>
                💡 <strong>¿Cómo puedo ayudarte?</strong>
            </p>
            <p>
                Este asistente está diseñado para responder consultas
                sobre <strong>turnos médicos</strong>,
                <strong>coberturas de salud</strong>,
                <strong>políticas de cancelación</strong>,
                <strong>privacidad de datos</strong>
                y más información sobre nuestra clínica.
            </p>
        </div>
        """
    )
    # ============================================

    display_chat_history()

    st.divider()

    col_chat, col_help = st.columns([9, 1])

    with col_chat:
        handle_user_input(rag_chain)

    with col_help:
        st.markdown(
            """
            <div style="text-align:center;padding-top:0.5rem;">
                <span
                    style="font-size:2rem;"
                    title="Presiona Enter para enviar">
                    ⏎
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_footer()

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()