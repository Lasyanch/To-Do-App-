import streamlit as st
import pandas as pd
import plotly.express as px

from database import get_tasks


st.title("📊 Analytics")

tasks = get_tasks()

if not tasks:
    st.warning("No data available")
    st.stop()

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

total_tasks = len(df)

completed = len(
    df[df["Status"] == "Completed"]
)

pending = len(
    df[df["Status"] == "Pending"]
)

completion_rate = (
    completed / total_tasks
) * 100

col1, col2, col3 = st.columns(3)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed)
col3.metric(
    "Completion Rate",
    f"{completion_rate:.1f}%"
)

st.subheader("Task Status")

fig1 = px.pie(
    df,
    names="Status",
    title="Completed vs Pending"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.subheader("Priority Distribution")

fig2 = px.bar(
    df["Priority"].value_counts(),
    title="Tasks by Priority"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)