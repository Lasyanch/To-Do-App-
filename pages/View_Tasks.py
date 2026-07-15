import streamlit as st
import pandas as pd

from datetime import datetime

from database import (
    get_tasks,
    get_task_by_id,
    update_task,
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


    # -------------------------------
    # DISPLAY ALL TASKS
    # -------------------------------

    st.subheader("All Tasks")

    st.dataframe(
        df,
        use_container_width=True
    )


    # -------------------------------
    # SELECT TASK
    # -------------------------------

    st.divider()

    st.subheader("Manage Task")


    task_id = st.selectbox(
        "Select Task ID",
        df["ID"]
    )


    selected_task = get_task_by_id(task_id)


    # -------------------------------
    # TASK ACTIONS
    # -------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        if st.button(
            "✅ Mark Complete",
            use_container_width=True
        ):

            update_status(
                task_id,
                "Completed"
            )

            st.success(
                "Task marked as completed!"
            )

            st.rerun()


    with col2:

        if st.button(
            "✏️ Edit Task",
            use_container_width=True
        ):

            st.session_state[
                "editing_task"
            ] = task_id


    with col3:

        if st.button(
            "🗑️ Delete Task",
            use_container_width=True
        ):

            delete_task(task_id)

            if (
                "editing_task"
                in st.session_state
                and
                st.session_state[
                    "editing_task"
                ] == task_id
            ):

                del st.session_state[
                    "editing_task"
                ]

            st.success(
                "Task deleted successfully!"
            )

            st.rerun()


    # -------------------------------
    # EDIT TASK FORM
    # -------------------------------

    if (
        "editing_task"
        in st.session_state
    ):

        editing_task_id = (
            st.session_state[
                "editing_task"
            ]
        )


        task = get_task_by_id(
            editing_task_id
        )


        if task:

            st.divider()

            st.subheader(
                f"✏️ Edit Task #{editing_task_id}"
            )


            task_id_value = task[0]

            task_title = task[1]

            task_description = task[2]

            task_priority = task[3]

            task_category = task[4]

            task_due_date = task[5]

            task_status = task[6]


            priority_options = [
                "Low",
                "Medium",
                "High"
            ]


            priority_index = (
                priority_options.index(
                    task_priority
                )
                if task_priority
                in priority_options
                else 0
            )


            try:

                due_date_value = (
                    datetime.strptime(
                        task_due_date,
                        "%Y-%m-%d"
                    ).date()
                )

            except (
                ValueError,
                TypeError
            ):

                due_date_value = (
                    datetime.today().date()
                )


            with st.form(
                "edit_task_form"
            ):

                edited_title = (
                    st.text_input(
                        "Task Title",
                        value=task_title
                    )
                )


                edited_description = (
                    st.text_area(
                        "Description",
                        value=(
                            task_description
                            or ""
                        )
                    )
                )


                edited_priority = (
                    st.selectbox(
                        "Priority",
                        priority_options,
                        index=priority_index
                    )
                )


                edited_category = (
                    st.text_input(
                        "Category",
                        value=(
                            task_category
                            or ""
                        )
                    )
                )


                edited_due_date = (
                    st.date_input(
                        "Due Date",
                        value=due_date_value
                    )
                )


                save_col, cancel_col = (
                    st.columns(2)
                )


                with save_col:

                    save_button = (
                        st.form_submit_button(
                            "💾 Save Changes",
                            use_container_width=True
                        )
                    )


                with cancel_col:

                    cancel_button = (
                        st.form_submit_button(
                            "❌ Cancel",
                            use_container_width=True
                        )
                    )


                if save_button:

                    if not edited_title.strip():

                        st.error(
                            "Task title is required"
                        )

                    else:

                        update_task(
                            task_id_value,
                            edited_title.strip(),
                            edited_description,
                            edited_priority,
                            edited_category,
                            str(
                                edited_due_date
                            )
                        )


                        del st.session_state[
                            "editing_task"
                        ]


                        st.success(
                            "Task updated successfully!"
                        )


                        st.rerun()


                if cancel_button:

                    del st.session_state[
                        "editing_task"
                    ]


                    st.rerun()


else:

    st.info("No Tasks Found")