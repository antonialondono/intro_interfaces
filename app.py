import streamlit as st
from PIL import Image

st.title("Creación de interfaces multimodales")
st.header("Holaaaa")
st.write("Tipos de letra")
image = Image.open('peces.jpg')

st.image(image, caption='Tipos de peces')

texto=st.text_input('Escribe algo','Este es mi texto')
st.write('El exto escrito es',texto)
