from gtts import gTTS
import streamlit as st
from io import BytesIO

# Entrada de texto de Streamlit
st.title("Generador de Audio de Textos")
text = st.text_area("Ingrese el texto:", height=200)

# Opción para ajustar la velocidad del audio
speed = st.slider("Velocidad de lectura", 0.5, 1.5, 1.0, step=0.1)

if st.button("Generar Audio"):
    if text:
        # Configura la velocidad con el parámetro 'slow'
        tts = gTTS(text=text, lang='es', slow=speed < 1.0)
        
        # Crear un flujo de bytes en memoria
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)  # Escribir el audio al flujo de bytes
        audio_bytes.seek(0)  # Mover al principio para poder leer
        
        st.success("Audio generado")
        st.audio(audio_bytes, format='audio/mp3')
        
        # Opción para que el usuario descargue el audio
        st.download_button(
            label="Descargar Audio",
            data=audio_bytes,
            file_name="audio.mp3",
            mime="audio/mp3"
        )
    else:
        st.error("Por favor, ingrese un texto.")
