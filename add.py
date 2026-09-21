import streamlit as st

st.title("Add two numbers")

a = st.number_input("First number", value=0.0)
b = st.number_input("Second number", value=0.0)

st.write("Sum:", a + b)