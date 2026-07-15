import streamlit as st
from database import add_task


st.title("➕ Add Task")

title = st.text_input("Task Title")

description = st.text_area("Description")

priority = st.selectbox(
    "Priority",
    ["Low", "Medium", "High"]
)

category = st.text_input("Category")

due_date = st.date_input("Due Date")

if st.button("Add Task"):

    if title:

        add_task(
            title,
            description,
            priority,
            category,
            str(due_date)
        )

        st.success("Task Added Successfully!")

    else:
        st.error("Title is required")