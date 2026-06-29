"""
theme.py

Responsabilidad:
    Definir y aplicar el sistema de estilos global de la aplicación Streamlit.
"""

import streamlit as st


def apply_custom_theme() -> None:
    """Aplica el tema visual global de la aplicación."""

    st.markdown(
        """
        <style>

        /* =====================================================
           BASE LAYOUT
        ===================================================== */

        .main {
            padding: 2rem;
        }

        /* =====================================================
           TYPOGRAPHY
        ===================================================== */

        .main-title {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(
                135deg,
                #00b4d8 0%,
                #0077b6 35%,
                #48cae4 100%
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #2b6777;
            font-weight: 500;
            margin-bottom: 1.5rem;
        }

        /* =====================================================
           CHAT MESSAGES
        ===================================================== */

        .user-message {
            background: linear-gradient(
                135deg,
                #00b4d8 0%,
                #0077b6 100%
            );
            color: white !important;
            padding: 1rem 1.5rem;
            border-radius: 18px 18px 4px 18px;
            margin: 0.5rem 0;
            max-width: 80%;
            margin-left: auto;
            box-shadow: 0 4px 12px rgba(0, 119, 182, 0.2);
            border: none;
        }

        .assistant-message {
            background: #f0f7fa;
            color: #1a3a4a;
            padding: 1rem 1.5rem;
            border-radius: 18px 18px 18px 4px;
            margin: 0.5rem 0;
            max-width: 80%;
            border-left: 4px solid #2ecc71;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }

        /* =====================================================
           INPUT
        ===================================================== */

        .stTextInput > div > div > input {
            border-radius: 25px !important;
            border: 2px solid #c8e6e9;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            transition: all 0.3s ease;
            background-color: white;
        }

        .stTextInput > div > div > input:focus {
            border-color: #00b4d8 !important;
            box-shadow: 0 0 0 3px rgba(0, 180, 216, 0.2);
        }

        /* =====================================================
           LOADING
        ===================================================== */

        .stSpinner > div {
            border-color: #00b4d8 transparent transparent transparent !important;
        }

        /* =====================================================
           CARDS / STATISTICS
        ===================================================== */

        .stat-card {
            background: linear-gradient(
                135deg,
                #f0f7fa 0%,
                #e8f4f8 100%
            );
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            text-align: center;
            margin: 0.5rem 0;
            border: 1px solid #c8e6e9;
        }

        .stat-card div {
            color: #1a3a4a;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #0077b6;
        }

        /* =====================================================
           BUTTONS
        ===================================================== */

        .stButton > button {
            border-radius: 20px !important;
            transition: all 0.3s ease !important;
        }

        .stButton > button:hover {
            transform: scale(0.98);
        }

        /* =====================================================
           INFO BOX
        ===================================================== */

        .info-box {
            background: linear-gradient(
                135deg,
                #e8f4f8 0%,
                #d4edda 100%
            );
            padding: 1rem 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            border-left: 4px solid #2ecc71;
        }

        .info-box p {
            margin: 0;
            color: #1a3a4a;
        }

        /* =====================================================
           SIDEBAR - ESTILOS AGREGADOS
        ===================================================== */

        .sidebar-section {
            background: #f0f7fa;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            border: 1px solid #c8e6e9;
        }

        .sidebar-section h2 {
            color: #0077b6 !important;
            margin-bottom: 0.3rem;
        }

        .sidebar-section h3,
        .sidebar-section .sidebar-title {
            color: #0077b6 !important;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .sidebar-section p {
            color: #1a3a4a !important;
            margin: 0.5rem 0;
        }

        .sidebar-section strong {
            color: #0077b6 !important;
        }

        .sidebar-section ul {
            color: #1a3a4a !important;
            padding-left: 1.5rem;
            margin: 0.5rem 0;
        }

        .sidebar-section ul li {
            color: #1a3a4a !important;
            margin-bottom: 0.3rem;
        }

        .sidebar-section span {
            color: #1a3a4a !important;
        }

        .sidebar-section .text-secondary {
            color: #5d8a9e !important;
            font-size: 0.8rem;
        }

        .sidebar-section .text-muted {
            color: #7f8c8d !important;
            font-size: 0.85rem;
        }

        /* =====================================================
           FOOTER
        ===================================================== */

        .footer {
            text-align: center;
            color: #5d8a9e;
            padding: 2rem 0 1rem 0;
            border-top: 2px solid #e8f4f8;
            margin-top: 2rem;
            font-size: 0.9rem;
        }

        .footer strong {
            color: #0077b6 !important;
        }

        .footer span {
            color: #5d8a9e !important;
        }

        /* =====================================================
           STATUS BADGES
        ===================================================== */

        .status-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .status-online {
            background: #d4edda;
            color: #155724;
        }

        .status-offline {
            background: #f8d7da;
            color: #721c24;
        }

        /* =====================================================
           METRICS
        ===================================================== */

        .metric-value {
            color: #0077b6;
            font-size: 1.5rem;
            font-weight: bold;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )