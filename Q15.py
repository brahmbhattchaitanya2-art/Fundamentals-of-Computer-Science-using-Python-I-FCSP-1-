import streamlit as st
import matplotlib.pyplot as plt
import random

st.title("Matplotlib Integration App")

n = st.number_input("Enter number of random points", min_value=1, step=1)

if st.button("Generate Scatter Plot"):

    x = [random.random() for _ in range(n)]
    y = [random.random() for _ in range(n)]

    plt.scatter(x, y)
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Random Scatter Plot")

    st.pyplot(plt)
