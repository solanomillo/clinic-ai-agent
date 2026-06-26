# app/ui/styles/theme.py
import streamlit as st

def apply_custom_theme():
    """Aplica el tema CSS personalizado con colores azul/verde"""
    
    st.markdown("""
    <style>
        /* Estilo general */
        .main {
            padding: 2rem;
        }
        
        /* Estilo para el título - Clínica */
        .main-title {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #00b4d8 0%, #0077b6 35%, #48cae4 100%);
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
        
        /* Estilo para mensajes del usuario */
        .user-message {
            background: linear-gradient(135deg, #00b4d8 0%, #0077b6 100%);
            color: white !important;
            padding: 1rem 1.5rem;
            border-radius: 18px 18px 4px 18px;
            margin: 0.5rem 0;
            max-width: 80%;
            margin-left: auto;
            box-shadow: 0 4px 12px rgba(0, 119, 182, 0.2);
            border: none;
        }
        
        /* Estilo para mensajes del asistente */
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
        
        /* Estilo para el input */
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
        
        /* Estilo para el spinner */
        .stSpinner > div {
            border-color: #00b4d8 transparent transparent transparent !important;
        }
        
        /* Estadísticas */
        .stat-card {
            background: linear-gradient(135deg, #f0f7fa 0%, #e8f4f8 100%);
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            text-align: center;
            margin: 0.5rem 0;
            border: 1px solid #c8e6e9;
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #0077b6;
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
            color: #5d8a9e;
            padding: 2rem 0 1rem 0;
            border-top: 2px solid #e8f4f8;
            margin-top: 2rem;
            font-size: 0.9rem;
        }
        
        .footer-icon {
            color: #2ecc71;
            font-size: 1.2rem;
        }
        
        /* Badge de estado */
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
        
        /* Estilo para la caja de información */
        .info-box {
            background: linear-gradient(135deg, #e8f4f8 0%, #d4edda 100%);
            padding: 1rem 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            border-left: 4px solid #2ecc71;
        }
        
        .info-box p {
            margin: 0;
            color: #1a3a4a;
        }
        
        /* Sidebar mejorado */
        .sidebar-section {
            background: #f8fcfe;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            border: 1px solid #e8f4f8;
        }
        
        .sidebar-title {
            color: #0077b6;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        
        /* Botones en sidebar */
        .stButton > button {
            border-radius: 20px !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            transform: scale(0.98);
        }
        
        /* Tasa de respuesta */
        .metric-value {
            color: #0077b6;
            font-size: 1.5rem;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)