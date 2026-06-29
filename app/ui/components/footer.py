"""
footer.py

Responsabilidad:
    Renderizar el pie de página de la aplicación.
"""

from __future__ import annotations

import streamlit as st


def render_footer() -> None:
    """
    Renderiza el pie de página de la aplicación.
    """

    st.html(
        """
        <div class="footer">
            <strong>Clinic AI Agent</strong>
            <br>
            Asistente inteligente para consultas institucionales
            basado en <strong>Retrieval-Augmented Generation (RAG)</strong>.
            <br><br>
            <strong>Tecnologías</strong>
            <br>
            Streamlit • LangChain • FAISS • Google Gemini • HuggingFace
            <br><br>
            <span style="font-size:0.8rem; color:#95a5a6;">
                Versión 1.0.0
            </span>
        </div>
        """
    )