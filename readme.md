# 📋 Smart To-Do Manager

A simple and user-friendly **To-Do List Dashboard** built with **Python**, **Streamlit**, **Pandas**, and **SQLite**. This application helps users organize tasks, monitor progress, and track overdue work through an interactive dashboard.

---

## 🚀 Features

- ✅ Add, view, edit, and delete tasks
- 📊 Dashboard with task statistics
- 📈 Overall completion progress bar
- 🔴 Automatic overdue task detection
- 📅 Due date management
- 🏷️ Task categorization
- ⚡ Priority levels (High, Medium, Low)
- ✔️ Task status tracking (Pending/Completed)
- 📌 Displays the five most recent tasks
- 💾 SQLite database for persistent storage
- 📱 Responsive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- SQLite
- Datetime

---

## 📂 Project Structure

```
Smart-ToDo-Manager/
│
├── app.py                 # Dashboard
├── database.py            # Database functions
├── data/
│   └── tasks.db           # SQLite database
├── pages/
│   ├── Add_Task.py
│   ├── View_Tasks.py
│   └── Analytics.py
├── requirements.txt
└── README.md
```

---

## 📊 Dashboard

The dashboard displays:

- Total Tasks
- Pending Tasks
- Completed Tasks
- Completion Percentage
- Overdue Tasks
- Progress Bar
- Recent Tasks
- Overdue Task List

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Smart-ToDo-Manager.git
```

### 2. Navigate to the project folder

```bash
cd Smart-ToDo-Manager
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 📦 Required Libraries

```
streamlit
pandas
sqlite3
```

> **Note:** `sqlite3` and `datetime` are built into Python and do not need to be installed separately.

---

## 🎯 Future Improvements

- 🔔 Task reminders and notifications
- 🌙 Dark mode
- 🔍 Search and advanced filters
- 📤 Export tasks to Excel/PDF
- ☁️ Cloud database integration
- 👤 User authentication
- 📅 Calendar view
- 📈 Advanced analytics and charts

---

## 🎓 Learning Objectives

This project demonstrates:

- CRUD operations using SQLite
- Streamlit web application development
- Data handling with Pandas
- Dashboard creation
- Progress tracking
- Date comparison using Python
- Basic database management

---

## 👩‍💻 Author

**Lasya**

B.Tech (AI & ML)

---

## ⭐ If you found this project helpful, consider giving it a star!