import sqlite3


DB_NAME = "data/tasks.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT,
        category TEXT,
        due_date TEXT,
        status TEXT DEFAULT 'Pending'
    )
    """)

    conn.commit()
    conn.close()


def add_task(title, description, priority, category, due_date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks
    (title, description, priority, category, due_date)
    VALUES (?, ?, ?, ?, ?)
    """,
    (title, description, priority, category, due_date))

    conn.commit()
    conn.close()


def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    conn.close()

    return rows


def update_status(task_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET status = ?
    WHERE id = ?
    """, (status, task_id))

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()