# FastAPI Project 🚀

Welcome to my FastAPI Project!  
This project is designed to help developers learn FastAPI by building a real-world backend application, progressing from basic concepts to intermediate and production-ready features.

## 📚 About This Project

This repository walks through three main phases of backend development using FastAPI:

### ✅ Version 1: Basic To-Do API
- Built using **FastAPI** and **SQLite**.
- Implements CRUD operations for To-Do items.
- Uses **APIRouter** to structure routes modularly.

### ✅ Version 2: Authentication & JWT
- Implements **User Authentication** with **OAuth2** and **JWT Tokens**.
- Passwords are hashed securely using **Passlib** with **bcrypt**.
- Users can:
  - Login & receive a JWT token.
  - Retrieve user details (excluding password).
  - Update their password securely.
- Protects routes with authentication dependencies.

### ✅ Version 3: Production-Ready Setup with PostgreSQL & Alembic
- Switched from SQLite to **PostgreSQL** for production-level database management.
- Integrated **Alembic** for database migrations.
- Added environment-based database configuration for flexibility and security.

---

## 🔥 Key Technologies Used
- **FastAPI** (Python Web Framework)
- **SQLAlchemy** (ORM)
- **PostgreSQL** (Database)
- **Alembic** (Database Migrations)
- **JWT** for Authentication
- **OAuth2PasswordBearer** for token-based authentication
- **bcrypt** (Password Hashing)
- **PgAdmin** for PostgreSQL Management

---

## 📂 Project Structure
fastapi_project/
│
├── ToDo-App/ # Main App Directory
│ ├── alembic/ # Alembic Migration Files
│ ├── alembic.ini # Alembic Config File
│ ├── routers/ # API Routers (auth, todos, users)
│ ├── models.py # SQLAlchemy Models
│ ├── database.py # DB Connection Setup
│ ├── main.py # FastAPI Entry Point
│ └── notes.md # My Learning Notes (Deep Dive)
│
├── .gitignore
└── README.md


---

## 🛠️ Getting Started

1. **Clone the repo**:
```bash
git clone https://github.com/ajith4Tech/fastapi_project.git
cd fastapi_project
```
2. **Set up virtual environment**:

```
python -m venv venv
source venv/bin/activate
```
3. **Install Dependencies**:

```
pip install -r requirements.txt
```

4. **Configure PostgreSQL Database**:

    - Create DB & User in PostgreSQL.

    - Update DB connection in alembic.ini and database.py:
```
SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@localhost/<dbname>"
```
    
5. **Run Alembic Migrations**:

```
alembic upgrade head
```
6. Run the App:
```
uvicorn main:app --reload
```

✍️ My Learning Notes

I have documented everything I've learned during this project including:

- Routers & Modularization

- JWT Authentication

- Password Hashing with Bcrypt

- OAuth2 Flows

- Alembic Migrations

- PostgreSQL Setup

➡️ Read My Full Notes Here : https://github.com/ajith4Tech/fastapi_project/blob/master/ToDo-App/Notes.md

🙌 Acknowledgements

- FastAPI Official Docs: https://fastapi.tiangolo.com/

- PostgreSQL Docs

- Alembic Migration Docs

⭐ Star the repo if you found it helpful!

🧑‍💻 Author
Curated by Ajith B M