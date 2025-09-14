import streamlit as st

def add(a, b):
    return a + b

# App title
st.title("🧱 Simple Calculator App with CI/CD")

# Add some description
st.markdown("This app performs simple addition of two numbers. Enter numbers below and click **Add**!")

# Create two input columns
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("🔢 First Number", value=0)

with col2:
    num2 = st.number_input("🔢 Second Number", value=0)

# Add button with a centered style
if st.button("➕ Add Numbers"):
    result = add(num1, num2)
    st.success(f"✅ The result of adding **{num1} + {num2}** is **{result}**")
