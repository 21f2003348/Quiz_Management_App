# 🧠 Quiz Management Web App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?logo=sqlite)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS-orange?logo=html5)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

---

>A full-stack **Quiz Management Web Application** built using **Flask**, developed as part of the **Modern Application Development (MAD1)** course at **IIT Madras**.  
>This project provides a complete system for user registration, quiz creation, participation, and score management — with separate dashboards for **Admin** and **Users**.

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
```
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
```

---

## ⚙️ Installation and Setup

Follow these steps to set up and run the project locally on your system:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/21f2003348/Quiz_Management_App.git
cd Quiz_Management_App
```

2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
3️⃣ Activate the Virtual Environment

  Windows:
```bash
venv\Scripts\activate
```

  macOS / Linux:
```bash
source venv/bin/activate
```
4️⃣ Install Project Dependencies

All necessary dependencies are listed in requirements.txt.
Install them using the command below:
```bash
pip install -r requirements.txt
```

If the file is missing, you can manually install key packages:
```bash
pip install flask flask-sqlalchemy flask-wtf flask-login flask-migrate
```
5️⃣ Initialize the Database

Run the following commands to set up the database (optional if database.db already exists):
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

Alternatively, just start the app — it will create database.db automatically if configured that way.

6️⃣ Run the Application
```bash
python app.py
```

Then open your browser and visit:
```bash
http://127.0.0.1:5000
```
📦 Requirements File

Below is the list of dependencies used in this project, also available in requirements.txt
:
```
Flask==3.0.3/n
Flask-WTF==1.2.1
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Flask-Migrate==4.0.7
WTForms==3.1.2
Werkzeug==3.0.4
Jinja2==3.1.4
itsdangerous==2.2.0
click==8.1.7
SQLAlchemy==2.0.34
```

Optional for testing and environment variables:
```bash
pytest==8.3.2
python-dotenv==1.0.1
```
📸 Screenshots (Optional)

Add screenshots inside an /assets/screenshots/ folder and reference them here:

![Login Page](assets/screenshots/login_page.png)
![Admin Dashboard](assets/screenshots/admin_dashboard.png)

🧩 Future Improvements

Email verification for user registration

Add quiz timers and leaderboards

Enhanced responsive design for mobile

Integration with PostgreSQL or Firebase

🤝 Contributing

Contributions are welcome!
If you’d like to improve this project:

Fork the repository

Create a new branch:
```bash
git checkout -b feature-name
```

Commit your changes:
```bash
git commit -m "Added new feature"
```

Push to your branch:
```bash
git push origin feature-name
```

Create a Pull Request

🧑‍💻 Author

Ansh Patel
Modern Application Development (MAD1) – IIT Madras
📂 GitHub: @21f2003348

📜 License

This project is licensed under the MIT License — feel free to use, modify, and distribute with attribution.

⭐ If you found this project useful, please give it a star on GitHub! ⭐
