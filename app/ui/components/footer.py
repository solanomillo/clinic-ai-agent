# app/ui/components/footer.py
import streamlit as st

def render_footer():
    """Renderiza el footer de la aplicación"""
    
    st.markdown("""
    <div class="footer">
        <div style="display: flex; justify-content: center; gap: 2rem; align-items: center; flex-wrap: wrap;">
            <span>🏥 <strong>Clínica AI</strong></span>
            <span>•</span>
            <span>🤖 <strong>Asistente Médico</strong></span>
            <span>•</span>
            <span>📚 <strong>RAG Architecture</strong></span>
            <span>•</span>
            <span>🔒 <strong>Datos Seguros</strong></span>
        </div>
        <div style="margin-top: 0.75rem; font-size: 0.85rem;">
            <span>❤️ Desarrollado para brindar información médica confiable</span>
        </div>
        <div style="margin-top: 0.5rem; font-size: 0.75rem; color: #95a5a6;">
            <span>⚠️ Esta herramienta es informativa. Consulta siempre a tu médico.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)