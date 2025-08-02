import streamlit as st
import pandas as pd

# Title
st.title("👋 Welcome to My Simple Website")

# Text
st.write("This is a basic web app made with Streamlit.")

# Image from a URL
st.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Google-flutter-logo.png", caption="A Sample Image")

# Small dataset
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)

# Show table
st.write("Here's a small table:")
st.dataframe(df)
