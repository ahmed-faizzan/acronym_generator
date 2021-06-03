import streamlit as st
from PIL import Image

def app():
    # st.subheader(""" Acronym Generator """)
    image = Image.open('acronym.png')
    st.image(image)
    