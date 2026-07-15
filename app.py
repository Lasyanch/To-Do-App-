import streamlit as st
from database import create_table

st.set_page_config(
    page_title="Smart To-Do Manager",
    page_icon="✅",
    layout="wide"
)

create_table()

st.title("✅ Smart To-Do Manager")

st.markdown("""
Welcome to your productivity dashboard.

Use the sidebar to:
- Add Tasks
- View Tasks
- Check Analytics
""")