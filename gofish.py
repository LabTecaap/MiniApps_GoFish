#import
import streamlit as st
from PIL import Image

#background
page_bg_img = '''<style>
[data-testid="stAppViewContainer"] {
background-color:#FFFFFF}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
colT1, colT2 = st.columns([1, 5])
with colT2:
  image = Image.open('gofish.jpg')
  st.image(image, width=400)

#option
especie_option = st.radio('Selecione a espécie em produção:', ('Tambaqui', 'Tilapia', 'Bagrinho'))

#textbox
peso_medio = st.number_input('Peso médio dos peixes (em gramas):')

#codigo
if especie_option == 'Tambaqui':
  if peso_medio  < 1:
    st.text('Sem resultados')
  if peso_medio >= 1 and peso_medio < 7:
    st.text('Para seu cultivo use ração em pó.')
  elif peso_medio >= 7 and peso_medio < 25:
    st.text('Para seu cultivo:\nUtilize ração com granulometria de 1mm a 2mm')
  elif peso_medio >= 25 and peso_medio < 69:
    st.text('Para seu cultivo:\nUtilize ração com granulometria de 2mm a 4mm')
  elif peso_medio >= 69 and peso_medio < 188:
    st.text('Para o seu cultivo:\nUtilize ração com granulometria de 4mm a 6mm')
  elif peso_medio >= 188:
    st.text('Para seu cultivo:\nUtilize ração com granulometria de  8mm')

if especie_option == 'Tilapia':
  if peso_medio  < 1:
    st.text('Sem resultados')
  if peso_medio >= 1 and peso_medio < 5:
    st.text('Para seu cultivo use ração em pó.')
  elif peso_medio >= 5 and peso_medio < 30:
    st.text('Para seu cultivo:\nUtilize ração com granulometria de 2,6mm')
  elif peso_medio >= 30 and peso_medio < 240:
    st.text('Para seu cultivo:\nUtilize ração com granulometria de 4mm')
  elif peso_medio >= 240:
    st.text('Para seu cultivo:\nUtilize ração com granulometria de 6mm a 8mm')

if especie_option == 'Bagrinho':
  if peso_medio  < 1:
    st.text('Sem resultados')
  if peso_medio >= 1 and peso_medio < 5:
    st.text('Para seu cultivo use ração em pó.')
  elif peso_medio >= 5 and peso_medio < 70:
    st.text('Para seu cultivo:\nUtilize ração com granulometria de 2,6mm')
  elif peso_medio >= 70 and peso_medio < 110:
    st.text('Para seu cultivo:\nUtilize ração com granulometria de 4mm')
  elif peso_medio >= 110:
    st.text('Para seu cultivo:\nUtilize ração com granulometria de 6mm a 8mm')
