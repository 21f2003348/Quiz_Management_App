# 🧠 Quiz Management Web App

A full-stack **Quiz Management Web Application** built using **Flask**, developed as part of the **Modern Application Development (MAD1)** course at **IIT Madras**.  
This project provides a complete system for user registration, quiz creation, participation, and score management — with separate dashboards for **Admin** and **Users**.

---

## 🚀 Features

### 👤 User Features
- Secure user registration and login (passwords stored with hashing)
- Attempt quizzes dynamically loaded from the database
- View quiz results and performance summaries
- Manage profile and logout securely

### 🧑‍💼 Admin Features
- Add, update, or delete subjects, quizzes, and questions
- Manage registered users and view statistics
- Control quiz visibility and access permissions
- Role-based access control via **Flask-Login**

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Flask (Python) |
| Frontend | HTML, CSS, Jinja2 Templates |
| Database | SQLite (via SQLAlchemy ORM) |
| Forms & Validation | Flask-WTF |
| Authentication | Flask-Login, Werkzeug Security |
| Database Migration | Flask-Migrate |

---

## 📁 Project Structure

Quiz_Management_App/
│
├── app.py # Main Flask application
├── models.py # Database models
├── forms.py # Form definitions (login, register, etc.)
├── requirements.txt # Project dependencies
├── instance/
│ └── database.db # SQLite database file
├── static/
│ └── style.css # Custom styles
├── templates/ # HTML templates
│ ├── base.html
│ ├── login.html
│ ├── register.html
│ ├── quiz.html
│ ├── user_dashboard.html
│ ├── admin_dashboard.html
│ ├── add_quiz.html
│ ├── add_question.html
│ └── ...
└── README.md


---

## ⚙️ Installation and Setup

Follow these steps to set up and run the project locally on your system:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/21f2003348/Quiz_Management_App.git
cd Quiz_Management_App

