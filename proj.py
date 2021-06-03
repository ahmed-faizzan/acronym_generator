import streamlit as st
from multiapp import MultiApp
from app import home, acro

app = MultiApp()
st.markdown (""" # ACRONYM GENERATOR """)

st.text("Use the dropdown menu to navigate between Homepage and Acronym Generator: ")

app.add_app("Homepage", home.app)
app.add_app("Acronym Generator", acro.app)

app.run()