import streamlit as st

def add(a, b):
    return a + b

st.title("Streamlit App with CI/CD")

num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

if st.button("Add"):
    st.write(f"Result: {add(num1, num2)}")
