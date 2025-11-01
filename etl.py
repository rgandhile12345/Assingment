import pandas as pd
import streamlit as st


data = {
    "Task": ["Extract", "Transform", "Load"],
    "Status": ["Completed", "Processing", "Pending"]
}

df = pd.DataFrame (data)
st.title("Streamlit App")
st.write(df)

