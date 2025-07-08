# 🚀 FastAPI Project

Welcome to my FastAPI Project!  
This project is designed to help developers learn FastAPI by building a real-world backend application, progressing from basic concepts to intermediate and production-ready features — now extended with **frontend integration** and **testing**!

---

## 📚 About This Project

This repository walks through **three main phases** of backend development using FastAPI, along with an added **frontend layer** and **testing suite**:

### ✅ Version 1: Basic To-Do API
- Built using **FastAPI** and **SQLite**.
- Implements **CRUD** operations for To-Do items.
- Uses **APIRouter** to structure routes modularly.

### ✅ Version 2: Authentication & JWT
- Implements **User Authentication** with **OAuth2** and **JWT Tokens**.
- Passwords are securely hashed using **Passlib** with **bcrypt**.
- Features:
  - Login with JWT Token issuance.
  - Retrieve user details (excluding password).
  - Password update functionality.
- Protected Routes with Authentication Dependencies.

### ✅ Version 3: Production-Ready Setup with PostgreSQL & Alembic
- Switched to **PostgreSQL** for production-grade DB.
- Integrated **Alembic** for database migrations.
- Environment-based DB configurations for flexibility and security.

### ✅ Version 4: Frontend Integration with Jinja2 + Bootstrap
- **Jinja2 Templates** for Server-side Rendering.
- **Bootstrap 5** for UI Styling.
- **Vanilla JavaScript** (Fetch API) for API interactions:
  - Registration & Login Forms.
  - Password Match Validation.
  - ToDo CRUD via Frontend.
  - JWT Cookie Management for Authenticated Actions.
- Static Files Management (CSS, JS, etc.) via **Starlette StaticFiles**.

---

### ✅ Version 5: Testing with Pytest
- Added **automated testing** using **Pytest** for APIs and authentication flows.
- Key Features:
  - Test DB setup using **SQLite in-memory**.
  - Test Cases Cover:
    - User Registration
    - JWT Authentication
    - ToDo CRUD APIs
  - FastAPI’s **TestClient** for HTTP requests simulation.
- Ensures reliability and future-proofing of the app.

---

## 🔥 Key Technologies Used
- **FastAPI** (Backend)
- **SQLAlchemy** (ORM)
- **PostgreSQL** (Database)
- **Alembic** (Migrations)
- **Jinja2** (Templating Engine)
- **Bootstrap 5** (UI Styling)
- **Vanilla JS** (Frontend Logic)
- **JWT** + **OAuth2PasswordBearer** (Authentication)
- **bcrypt** (Password Hashing)
- **aiofiles** + **Starlette StaticFiles** (Static Asset Management)
- **Pytest** (Testing Framework)

---

## 📂 Project Structure

fastapi_project/
│
├── ToDo-App/ # Main App Directory
│ ├── alembic/ # Alembic Migration Files
│ ├── alembic.ini # Alembic Config File
│ ├── routers/ # API Routers (auth, todos, users, admin)
│ ├── models.py # SQLAlchemy Models
│ ├── database.py # DB Connection Setup
│ ├── main.py # FastAPI Entry Point
│ ├── templates/ # Jinja2 Templates (HTML Pages)
│ │ ├── layout.html # Base Layout
│ │ ├── home.html # Homepage
│ │ ├── auth/ # Login, Register Pages
│ │ └── todos/ # ToDo Pages (CRUD)
│ ├── static/ # Static Files (CSS, JS, Bootstrap Assets)
│ │ ├── css/ # Stylesheets
│ │ └── js/ # JavaScript Files (Fetch API Logic)
│ └── notes.md # My Learning Notes
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

- Jinja2 Templating & Frontend Integration

➡️ Read My Full Notes Here : https://github.com/ajith4Tech/fastapi_project/blob/master/ToDo-App/Notes.md

🙌 Acknowledgements

- FastAPI Official Docs: https://fastapi.tiangolo.com/

- PostgreSQL Docs

- Alembic Migration Docs

- Pytest Docs
 
- Bootstrap Docs

⭐ Star the repo if you found it helpful!

🧑‍💻 Author
Curated by Ajith B M