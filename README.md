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

## Database

The application uses PostgreSQL.

- Local development uses the `DATABASE_URL` environment variable.
- Production database is hosted on Render PostgreSQL.
- Database credentials are stored in `.env` and are not committed to Git.




## Live API

**Swagger UI:** https://job-tracker-api-b3t8.onrender.com/docs

**API Base URL:** https://job-tracker-api-b3t8.onrender.com