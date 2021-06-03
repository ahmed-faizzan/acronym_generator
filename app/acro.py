import streamlit as st

def app():
    # st.header("Acronym Generator")
    user_input = st.text_input("Enter a Phrase to Make Acronym")
    text = user_input.split()
    a = " "
    for i in text:
        a = a+str(i[0]).upper()
    st.subheader(f'Acronym of {user_input} is {a}')
    # st.write(f'Acronym of {user_input} is {a}')