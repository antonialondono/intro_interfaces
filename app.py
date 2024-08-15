import streamlit as st
from PIL import Image

st.title("Creación de interfaces multimodales")
st.header("Holaaaa")
st.write("Tipos de letra")
image = Image.open('peces.jpg')

st.image(image, caption='Tipos de peces')

texto=st.text_input('Escribe algo','Este es mi texto')
st.write('El exto escrito es',texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz",('visual','auditiva','táctil'))
  if modo == 'visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'auditiva':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'táctil':
    st.write('El tacto es fundamental para tu interfaz')

st.subheader("Uso de botones")
if st.button ('Presiona el botón'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aún')
