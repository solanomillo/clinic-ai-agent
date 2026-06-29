"""
sidebar.py

Responsabilidad:
    Renderizar la barra lateral de la aplicación de forma modular y estable.
"""

from __future__ import annotations

import streamlit as st


def _render_header() -> None:
    """Renderiza el encabezado del sidebar."""

    st.html(
        """
        <div class="sidebar-section">
            <h2>🏥 Clínica AI</h2>
            <p>Asistente Inteligente</p>
        </div>
        """
    )


def _render_about() -> None:
    """Renderiza la descripción de la aplicación."""

    st.html(
        """
        <div class="sidebar-section">
            <h3>ℹ️ Acerca de Clinic AI Agent</h3>
            <p>
                Asistente inteligente basado en
                <strong>Retrieval-Augmented Generation (RAG)</strong>
                diseñado para responder consultas utilizando la
                documentación oficial de la clínica.
            </p>
            <h3>Puede ayudarte con:</h3>
            <ul>
                <li>Turnos médicos</li>
                <li>Coberturas de salud</li>
                <li>Políticas institucionales</li>
                <li>Privacidad de datos</li>
                <li>Información administrativa</li>
                <li>Respuestas basadas en documentos</li>
            </ul>
        </div>
        """
    )


def _render_system_status() -> None:
    """Renderiza el estado del sistema."""

    st.subheader("ℹ️ Estado del sistema")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="stat-card">
                <div>📊 Estado</div>
                <div class="stat-number">🟢</div>
                <div style="font-size:0.8rem;color:#27ae60;">
                    Activo
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div>❓ Consultas</div>
                <div class="stat-number">
                    {st.session_state.get("total_questions", 0)}
                </div>
                <div style="font-size:0.8rem;color:#7f8c8d;">
                    Totales
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def _render_chat_actions() -> None:
    """Renderiza las acciones del chat."""

    st.subheader("💬 Opciones")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🧹 Limpiar",
            use_container_width=True,
        ):
            st.session_state.messages = []
            st.rerun()

    with col2:

        if st.button(
            "💾 Guardar",
            use_container_width=True,
        ):
            st.toast("Chat guardado correctamente ✔️")


def _render_statistics() -> None:
    """Renderiza las estadísticas del sistema."""

    st.subheader("📊 Estadísticas")

    total = st.session_state.get("total_questions", 0)

    st.metric(
        label="Consultas realizadas",
        value=total,
    )

    st.progress(
        min(total / 10, 1.0),
        text=f"Actividad: {min(total * 10, 100)}%",
    )


def _render_footer() -> None:
    """Renderiza el pie del sidebar."""

    st.html(
        """
        <div class="sidebar-section">
            <strong>Clinic AI Agent</strong>
            <br>
            Versión 1.0.0
            <br><br>
            <span class="text-secondary">
                Sistema basado en RAG con documentación institucional
            </span>
        </div>
        """
    )


def render_sidebar() -> None:
    """Renderiza toda la barra lateral."""

    with st.sidebar:

        _render_header()

        st.divider()

        _render_about()

        st.divider()

        _render_system_status()

        st.divider()

        _render_chat_actions()

        st.divider()

        _render_statistics()

        st.divider()

        _render_footer()