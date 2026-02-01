# Regalo Isa Cumpleaños

import streamlit as st
from datetime import datetime
import time

# Configuración de la página Móvil
st.set_page_config(
    page_title="Our story :D ❤️",
    page_icon="🐰",
    layout="centered"
)

# --- CONFIGURACIÓN ---
# Ajusta tu fecha aquí: (Año, Mes, Día, Hora, Minuto)
FECHA_INICIO = datetime(2025, 8, 1, 0, 0)
NOMBRE = "My Bunny"
FOTO_PATH = "FrontalFoto.jpg"

# CSS
st.markdown("""
    <style>
    .main {
        background-color: #fdf2f2;
    }
    .stText, .stMarkdown, h1, h2, h3 {
        text-align: center;
        color: #d32f2f !important;
    }
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
        color: #d32f2f;
    }
    </style>
    """, unsafe_allow_html=True)

# Título
st.title(f"For {NOMBRE} with love ❤️")

# Mostrar Foto
try:
    st.image("Regalo/FrontalFoto.jpg", use_container_width=True, caption="My favorite picture of us")
except:
    st.warning("FrontalFoto.jpg")

st.divider()

# Cálculo de tiempo (Contador dinámico)
st.subheader("We've been together for:")

# Cambio nuevo
st.divider() # Una línea sutil de separación

# Puedes usar st.write o st.markdown para darle estilo
st.markdown("""
    ### Mi dedicatoria para ti 💌
    Aquí puedes escribir todo lo que sientas. Por ejemplo:
    
    *Gracias por estos meses increíbles a tu lado. Eres la persona que ilumina mis días 
    y no puedo esperar para seguir sumando segundos, minutos y horas contigo.*
    
    **I love you so much**
    """, unsafe_allow_html=True)

st.divider()

# Esto crea un contenedor que se actualiza
placeholder = st.empty()

# Bucle para que el segundero se mueva
while True:
    ahora = datetime.now()
    diferencia = ahora - FECHA_INICIO
    
    dias = diferencia.days
    horas = diferencia.seconds // 3600
    minutos = (diferencia.seconds // 60) % 60
    segundos = diferencia.seconds % 60
    
    with placeholder.container():
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Días", dias)
        col2.metric("Hrs", horas)
        col3.metric("Min", minutos)
        col4.metric("Seg", segundos)
        
        st.markdown(f"<p class='big-font'>Every second with you feels special</p>", unsafe_allow_html=True)
    
    time.sleep(1)