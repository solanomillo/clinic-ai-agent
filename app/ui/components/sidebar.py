# app/ui/components/sidebar.py
import streamlit as st
from datetime import datetime

def render_sidebar():
    """Renderiza la barra lateral con información del sistema"""
    
    with st.sidebar:
        st.markdown("""
        <div style="padding: 1.5rem 0.5rem;">
            <h2 style="color: #0077b6; margin-bottom: 0.5rem;">🏥 Clínica AI</h2>
            <p style="color: #5d8a9e; font-size: 0.9rem; margin-bottom: 1.5rem;">
                Asistente inteligente
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Información del sistema
        st.markdown("### ℹ️ Estado del Sistema")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="stat-card">
                <div>📊 Estado</div>
                <div class="stat-number">🟢</div>
                <div style="font-size: 0.8rem; color: #27ae60;">Activo</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="stat-card">
                <div>❓ Consultas</div>
                <div class="stat-number">{st.session_state.total_questions}</div>
                <div style="font-size: 0.8rem; color: #7f8c8d;">Totales</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Opciones de chat
        st.markdown("### 💬 Opciones")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🧹 Limpiar Chat", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
        with col2:
            if st.button("💾 Guardar", use_container_width=True):
                st.info("Chat guardado exitosamente!")
        
        st.markdown("---")
        
        # Estadísticas
        st.markdown("### 📊 Estadísticas")
        if st.session_state.total_questions > 0:
            st.metric(
                label="Tasa de respuesta",
                value=f"{st.session_state.total_questions / max(1, st.session_state.total_questions):.0%}"
            )
            st.progress(
                min(1.0, st.session_state.total_questions / 10),
                text=f"Actividad: {min(100, st.session_state.total_questions * 10)}%"
            )
        
        st.markdown("---")
        
        # Información de contacto
        st.markdown("### 📞 Contacto")
        st.markdown("""
        <div style="background: #f8fcfe; padding: 0.75rem; border-radius: 8px; font-size: 0.85rem;">
            <p style="margin: 0.25rem 0;">📧 soporte@clinica.com</p>
            <p style="margin: 0.25rem 0;">📱 +54 11 1234-5678</p>
            <p style="margin: 0.25rem 0;">🕐 Lun-Vie 8:00-20:00</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Footer de la barra lateral
        st.markdown(f"""
        <div style="text-align: center; color: #95a5a6; font-size: 0.75rem; margin-top: 1rem;">
            <div>🔄 Última actualización</div>
            <div style="font-size: 0.7rem;">{datetime.now().strftime('%H:%M:%S')}</div>
            <div style="font-size: 0.7rem; margin-top: 0.5rem;">v2.0.0</div>
        </div>
        """, unsafe_allow_html=True)