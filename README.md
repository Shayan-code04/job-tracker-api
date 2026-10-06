# Job Tracker API

A RESTful backend API for managing and tracking job applications.

Built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**, this project provides user authentication, job application management, filtering, analytics, and AI integration through a secure API.

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
- Gemini AI integration
- AI-powered prompt endpoint
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
- **Google Gemini API**

---

## 📁 Project Structure

```text
job-tracker-api/
│
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   ├── jobs.py
│   │   └── ai.py
│   │
│   ├── crud.py
│   ├── database.py
│   ├── gemini.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt