# Job Tracker API

A RESTful backend API for managing and tracking job applications.

Built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**, this project provides user authentication, job application management, filtering, and analytics through a secure API.

---

## 🚀 Features

- User registration and authentication
- JWT (JSON Web Token) based authentication
- Secure password hashing
- Create job applications
- View job applications
- Filter jobs by status
- View individual job applications
- Update job applications
- Delete job applications
- User-specific job access
- Job application analytics
- Automatic API documentation with Swagger UI
- PostgreSQL database integration
- Environment-based configuration

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Pydantic**
- **JWT Authentication**
- **Passlib / bcrypt**
- **Uvicorn**
- **python-dotenv**

---

## 📁 Project Structure
job-tracker-api/
│
├── app/
│   ├── models/
│   │   ├── job.py
│   │   └── user.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   └── jobs.py
│   │
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   └── schemas.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

