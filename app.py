import streamlit as st
import pandas as pd

from datetime import datetime, date

from database import create_table, get_tasks

create_table()

st.set_page_config(
    page_title="To-Do Dashboard",
    page_icon="✅",
    layout="wide"
)

st.title("📋 Dashboard")
st.caption("Manage your daily tasks efficiently.")

tasks = get_tasks()

# -------------------------------------------------------
# LOAD TASKS
# -------------------------------------------------------

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

else:

    df = pd.DataFrame(
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

# -------------------------------------------------------
# CALCULATE METRICS
# -------------------------------------------------------

today = date.today()

total = len(df)

completed = len(df[df["Status"] == "Completed"])

pending = total - completed

completion_rate = (completed / total) * 100 if total else 0

overdue = 0

overdue_status = []

days_overdue = []

for _, task in df.iterrows():

    try:

        due = datetime.strptime(
            str(task["Due Date"]),
            "%Y-%m-%d"
        ).date()

    except:

        due = None

    if (
        due
        and due < today
        and task["Status"] != "Completed"
    ):

        overdue += 1

        overdue_status.append("🔴 Overdue")

        days = (today - due).days

        days_overdue.append(f"{days} day(s)")

    else:

        overdue_status.append("")

        days_overdue.append("")

if not df.empty:

    df["Overdue"] = overdue_status

    df["Late By"] = days_overdue

# -------------------------------------------------------
# DASHBOARD METRICS
# -------------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Tasks",
    total
)

col2.metric(
    "Pending",
    pending
)

col3.metric(
    "Completed",
    completed
)

col4.metric(
    "Completion",
    f"{completion_rate:.1f}%"
)

col5.metric(
    "Overdue",
    overdue
)

st.divider()

# -------------------------------------------------------
# PROGRESS BAR
# -------------------------------------------------------

st.subheader("Overall Progress")

st.progress(completion_rate / 100)

st.write(
    f"**{completed} of {total} tasks completed**"
)

st.divider()

# -------------------------------------------------------
# RECENT TASKS
# -------------------------------------------------------

st.subheader("Recent Tasks")

if not df.empty:

    recent = (
        df.sort_values(
            "ID",
            ascending=False
        )
        .head(5)
    )

    def highlight_overdue(row):

        if row["Overdue"] == "🔴 Overdue":

            return [
               "font-weight: bold;"
            ] * len(row)

        return [
            ""
        ] * len(row)

    st.dataframe(
        recent.style.apply(
            highlight_overdue,
            axis=1
        ),
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No tasks available.")

st.divider()

# -------------------------------------------------------
# OVERDUE TASKS
# -------------------------------------------------------

st.subheader("🔴 Overdue Tasks")

if overdue:

    overdue_df = df[df["Overdue"] == "🔴 Overdue"]

    st.dataframe(
        overdue_df[
            [
                "Title",
                "Priority",
                "Due Date",
                "Late By"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

else:

    st.success("🎉 No overdue tasks.")