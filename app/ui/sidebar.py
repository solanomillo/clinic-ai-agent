"""
sidebar.py

Responsabilidad:
    Renderizar la barra lateral de la aplicación.
"""

from __future__ import annotations

from datetime import datetime

import streamlit as st


def render_sidebar() -> None:
    """
    Renderiza el sidebar de la aplicación.
    """

    with st.sidebar:

        st.markdown(
            '<div class="sidebar-content">',
            unsafe_allow_html=True
        )

        # --------------------------------------------------
        # Título
        # --------------------------------------------------

        st.markdown(
            "## 🤖 RAG Assistant"
        )

        st.divider()

        # --------------------------------------------------
        # Estado
        # --------------------------------------------------

        st.markdown(
            "### ℹ️ Información del Sistema"
        )

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
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
<div class="stat-card">
<div>❓ Preguntas</div>
<div class="stat-number">
{st.session_state.total_questions}
</div>
<div style="font-size:0.8rem;color:#7f8c8d;">
Totales
</div>
</div>
""",
                unsafe_allow_html=True
            )

        st.divider()

        # --------------------------------------------------
        # Botones
        # --------------------------------------------------

        st.markdown(
            "### 💬 Opciones"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🧹 Limpiar",
                use_container_width=True
            ):

                st.session_state.messages = []

                st.rerun()

        with col2:

            if st.button(
                "💾 Guardar",
                use_container_width=True
            ):

                st.info(
                    "Chat guardado."
                )

        st.divider()

        # --------------------------------------------------
        # Estadísticas
        # --------------------------------------------------

        st.markdown(
            "### 📊 Estadísticas"
        )

        if st.session_state.total_questions > 0:

            st.metric(
                "Preguntas",
                st.session_state.total_questions
            )

            progreso = min(
                1.0,
                st.session_state.total_questions / 10
            )

            st.progress(
                progreso,
                text=f"{int(progreso*100)}%"
            )

        st.divider()

        # --------------------------------------------------
        # Footer
        # --------------------------------------------------

        st.markdown(
            f"""
<div
style="
text-align:center;
font-size:.8rem;
color:#95a5a6;
">

🔄 {datetime.now().strftime("%H:%M:%S")}

<br>

v1.0.0

</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )