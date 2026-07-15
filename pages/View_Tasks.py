import streamlit as st
import pandas as pd

from database import (
    get_tasks,
    update_status,
    delete_task
)

st.title("📋 View Tasks")

tasks = get_tasks()

if tasks:

    df = pd.DataFrame(
        tasks,
        columns=[
            "ID",
            "Title",
            "Description",
            "Priority",
            "Category",
            "Due Date",
            "Status"
        ]
    )

    st.dataframe(df)

    task_id = st.selectbox(
        "Select Task ID",
        df["ID"]
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Mark Complete"):
            update_status(task_id, "Completed")
            st.success("Task Updated")

    with col2:

        if st.button("Delete Task"):
            delete_task(task_id)
            st.success("Task Deleted")

else:
    st.info("No Tasks Found")