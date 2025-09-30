import streamlit as st
import pandas as pd

st.title("🎬 Movie Recommendation System")
st.write("This is a demo of a recommendation system model.")

# Example input
user_id = st.number_input("Enter User ID", min_value=1, step=1)

if st.button("Recommend Movies"):
    st.success(f"Top recommendations for User {user_id}:")
    # Placeholder recommendations
    st.write(["Movie A", "Movie B", "Movie C"])
