# print("Message Processor Application") 
# print("Version 2.0")
# print("Updates work correctly")

import streamlit as st 
st.title("Fun Application")
message = st.text_input("Enter Anything")
if st.button("Go"):
    st.write("You entered:")
    st.write("Gali") 