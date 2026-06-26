"""
header.py

Responsabilidad:
    Renderizar el encabezado y pie
    de la aplicación.
"""

from __future__ import annotations

import streamlit as st


def render_header() -> None:
    """
    Renderiza el encabezado principal.
    """

    st.markdown(
        '<div class="main">',
        unsafe_allow_html=True
    )

    st.markdown(
        """
<h1 class="main-title">
🏥 CliniAsistente
</h1>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div
style="
background:#f8f9fa;
padding:1rem 1.5rem;
border-radius:10px;
margin-bottom:2rem;
border-left:4px solid #667eea;
">

<p
style="
margin:0;
color:#2c3e50;
">

💡
<strong>

Tu agente inteligente para gestión de turnos, coberturas y normativas.

</strong>

Responde únicamente utilizando
la documentación disponible.

</p>

</div>
""",
        unsafe_allow_html=True
    )


def render_footer() -> None:
    """
    Renderiza el pie de página.
    """

    st.markdown(
        """
<div class="footer">

<div
style="
display:flex;
justify-content:center;
gap:2rem;
">

<span>🤖 LangChain</span>

<span>•</span>

<span>📚 Agentic RAG</span>

<span>•</span>

<span>☁️ Oracle Cloud</span>

</div>

<div
style="
margin-top:.5rem;
">

Proyecto desarrollado
con Python + Streamlit

</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )