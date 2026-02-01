# Regalo Isa Cumpleaños

import streamlit as st
from datetime import datetime
import time

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Our Story ❤️", page_icon="🌹", layout="centered")

# 2. CSS PARA LA TRANSICIÓN Y DISEÑO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');

    .main {
        background: linear-gradient(135deg, #fff5f5 0%, #fed7e2 100%);
    }

    /* Animación de entrada suave */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .fade-in-content {
        animation: fadeIn 2s ease-out;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 2rem;
        text-align: center;
    }

    h1 {
        font-family: 'Dancing Script', cursive;
        color: #ff4b4b;
        font-size: 4rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }

    .timer-box {
        background: #ff4b4b;
        color: white;
        border-radius: 15px;
        padding: 15px;
        margin: 5px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE LA INTRO ---
if 'intro_done' not in st.session_state:
    placeholder_intro = st.empty()
    with placeholder_intro.container():
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        # Mensaje de intro con su propia animación
        st.markdown("""
            <h2 style='text-align: center; font-family: "Poppins"; color: #ff4b4b; animation: fadeIn 2.5s;'>
                This is for you, my love...
            </h2>
            """, unsafe_allow_html=True)
        time.sleep(3.5) 
    
    st.session_state.intro_done = True
    placeholder_intro.empty()
    st.rerun() # Esto fuerza la recarga para mostrar el contenido principal

# --- CONTENIDO PRINCIPAL (Aparece tras la intro) ---
# Envolvemos todo en un div con la clase 'fade-in-content'
st.markdown('<div class="fade-in-content">', unsafe_allow_html=True)

st.snow() # Los copos aparecen justo al empezar la transición

st.markdown("<h1>For My Bunny ❤️</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    try:
        st.image("Regalo/FrontalFoto.jpg", use_container_width=True)
    except:
        st.image("FrontalFoto.jpg", use_container_width=True)

with col2:
    st.markdown("""
        <div class='glass-card' style='padding: 1.5rem; margin-top: 10px;'>
            <p style='font-family: "Poppins"; font-size: 1.1rem; font-style: italic;'>
                "In you, I've found everything I wasn't even looking for."
            </p>
            <p style='font-size: 2rem;'>💍🌹✨</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown(f"""
    <div class="glass-card">
        <h2 style='font-family: "Dancing Script"; color: #ff4b4b;'>Our Promise</h2>
        <p style='font-family: "Poppins"; color: #4a4a4a;'>
            Since August 1st, 2025, my world has been brighter. Thank you for being my support, 
            my favorite laugh, and my home. No matter how much time passes, 
            I will always choose you over and over again. You are the love of my life.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; font-family: \"Poppins\";'>Infinite seconds together:</h3>", unsafe_allow_html=True)

# ---------------------------------------------------------
# LÓGICA DEL CONTADOR
# ---------------------------------------------------------
FECHA_INICIO = datetime(2025, 8, 1, 0, 0)
placeholder_timer = st.empty()

# Cerramos el div de la animación de entrada antes del bucle infinito
st.markdown('</div>', unsafe_allow_html=True)

while True:
    ahora = datetime.now()
    diff = ahora - FECHA_INICIO
    
    dias = diff.days
    horas, rem = divmod(diff.seconds, 3600)
    minutos, segundos = divmod(rem, 60)
    
    with placeholder_timer.container():
        c1, c2, c3, c4 = st.columns(4)
        c1.markdown(f"<div class='timer-box'><b>{dias}</b><br><small>DAYS</small></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='timer-box'><b>{horas}</b><br><small>HRS</small></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='timer-box'><b>{minutos}</b><br><small>MIN</small></div>", unsafe_allow_html=True)
        c4.markdown(f"<div class='timer-box'><b>{segundos}</b><br><small>SEC</small></div>", unsafe_allow_html=True)
        
        quotes = ["I love you more than yesterday", "You're my favorite place", "Always you", "To a thousand more years"]
        current_quote = quotes[segundos % len(quotes)]
        st.markdown(f"<p style='text-align: center; margin-top: 20px; font-family: \"Dancing Script\"; font-size: 1.5rem; color: #ff4b4b;'>{current_quote}</p>", unsafe_allow_html=True)
        
    time.sleep(1)