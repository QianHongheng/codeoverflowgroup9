import streamlit as st

# Set the title of the app
st.title("My First Streamlit App")

# Add a header
st.header("Welcome to my Streamlit website!")

# Add some text
st.write("This is a basic example of a Streamlit app.")

# Add a button
if st.button('Say hello'):
    st.write('Hello, Streamlit!')

# Add a slider
number = st.slider("Select a number", 0, 100)
st.write(f"You selected: {number}")

# Add a chart
import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(1, 100, size=10)
})

# Display a line chart
st.line_chart(df)
