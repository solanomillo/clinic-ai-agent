"""
styles.py

Responsabilidad:
    Aplicar todos los estilos CSS de la aplicación.
"""

from __future__ import annotations

import streamlit as st


def aplicar_estilos() -> None:
    """
    Inyecta el CSS personalizado de la aplicación.
    """

    st.markdown(
        """
<style>

.main {
    padding: 2rem;
}

.main-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(
        135deg,
        #667eea 0%,
        #764ba2 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
}

.user-message {
    background: linear-gradient(
        135deg,
        #667eea 0%,
        #764ba2 100%
    );
    color: white !important;
    padding: 1rem;
    border-radius: 15px;
    margin: .5rem 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 4px 6px rgba(
        0,
        0,
        0,
        .10
    );
}

.assistant-message {

    background: #f8f9fa;

    color: #2c3e50;

    padding: 1rem;

    border-radius: 15px;

    margin: .5rem 0;

    max-width: 80%;

    border-left: 4px solid #667eea;

    box-shadow: 0 4px 6px rgba(
        0,
        0,
        0,
        .05
    );
}

.stTextInput input {

    border-radius: 25px !important;

    border: 2px solid #e0e0e0;

    padding: .75rem 1.5rem;

    transition: all .3s;
}

.sidebar-content {

    padding: 1.5rem 1rem;
}

.stat-card {

    background: white;

    padding: 1rem;

    border-radius: 10px;

    text-align: center;

    box-shadow: 0 2px 4px rgba(
        0,
        0,
        0,
        .05
    );
}

.stat-number {

    font-size: 2rem;

    font-weight: bold;

    color: #667eea;
}

.footer {

    text-align: center;

    color: #95a5a6;

    padding: 2rem 0 1rem;

    margin-top: 2rem;

    border-top: 1px solid #ecf0f1;
}

</style>
        """,
        unsafe_allow_html=True
    )