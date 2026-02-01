# Regalo Isa Cumpleaños

import streamlit as st
from datetime import datetime
import time
import random

# 1. CONFIGURACIÓN E INYECCIÓN DE EFECTOS
st.set_page_config(page_title="Nuestra Historia ❤️", page_icon="🌹", layout="centered")

# Lanzar confeti al cargar
st.snow() # Efecto de nieve/partículas inicial

# 2. CSS AVANZADO (Diseño Glassmorphism y Animaciones)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');

    .main {
        background: linear-gradient(135deg, #fff5f5 0%, #fed7e2 100%);
    }

    /* Tarjetas estilo Cristal */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 2rem;
        text-align: center;
        animation: fadeIn 2s;
    }

    h1 {
        font-family: 'Dancing Script', cursive;
        color: #ff4b4b;
        font-size: 4rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    .timer-box {
        background: #ff4b4b;
        color: white;
        border-radius: 15px;
        padding: 15px;
        margin: 5px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA Y FOTO
st.markdown("<h1 style='text-align: center;'>For My Bunny ❤️</h1>", unsafe_allow_html=True)

col_img, col_text = st.columns([1, 1])

with col_img:
    try:
        # Intenta cargar la foto desde la ruta que definimos antes
        st.image("Regalo/FrontalFoto.jpg", use_container_width=True)
    except:
        st.image("FrontalFoto.jpg", use_container_width=True)

with col_text:
    st.markdown("""
        <div class='glass-card' style='padding: 1rem;'>
            <p style='font-family: "Poppins"; font-size: 1.1rem;'>
                "Encontré en ti todo lo que no sabía que estaba buscando."
            </p>
            <p style='font-size: 2rem;'>💍🌹✨</p>
        </div>
        """, unsafe_allow_html=True)

# 4. DEDICATORIA EXTENDIDA
st.markdown(f"""
    <div class="glass-card">
        <h2 style='font-family: "Dancing Script"; color: #ff4b4b;'>Nuestra Promesa</h2>
        <p style='font-family: "Poppins"; color: #4a4a4a;'>
            Desde el 1 de agosto de 2025, mi mundo cambió de color. Gracias por ser mi apoyo, 
            mi risa favorita y mi hogar. No importa cuánto tiempo pase, siempre elegiré 
            volver a ti una y otra vez. Eres el amor de mi vida.
        </p>
    </div>
    """, unsafe_allow_html=True)

# 5. CONTADOR DINÁMICO MEJORADO
st.markdown("<h3 style='text-align: center; font-family: \"Poppins\";'>Infinite Seconds Together:</h3>", unsafe_allow_html=True)

FECHA_INICIO = datetime(2025, 8, 1, 0, 0)
placeholder = st.empty()

# Bucle infinito del contador
while True:
    ahora = datetime.now()
    diff = ahora - FECHA_INICIO
    
    dias = diff.days
    horas, rem = divmod(diff.seconds, 3600)
    minutos, segundos = divmod(rem, 60)
    
    with placeholder.container():
        # Diseño de columnas para el contador
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown(f"<div class='timer-box'><b>{dias}</b><br>Días</div>", unsafe_allow_html=True)
        with c2: st.markdown(f"<div class='timer-box'><b>{horas}</b><br>Horas</div>", unsafe_allow_html=True)
        with c3: st.markdown(f"<div class='timer-box'><b>{minutos}</b><br>Min</div>", unsafe_allow_html=True)
        with c4: st.markdown(f"<div class='timer-box'><b>{segundos}</b><br>Seg</div>", unsafe_allow_html=True)
        
        # Frases aleatorias que cambian (Toque extra)
        frases = ["Te amo más que ayer", "Eres mi lugar favorito", "Siempre tú", "A por mil años más"]
        frase_hoy = frases[segundos % len(frases)]
        st.markdown(f"<p style='text-align: center; margin-top: 20px; font-style: italic; color: #ff4b4b;'>{frase_hoy}</p>", unsafe_allow_html=True)
        
    time.sleep(1)