# 🗒️ Notes API (Django REST Framework)

This is a simple Notes API built with Django and Django REST Framework.  
It allows authenticated users to register, login, and perform CRUD operations on their personal notes.

---

## 🚀 Features

- User registration and JWT authentication
- Token-based login/logout system
- Notes CRUD (Create, Read, Update, Delete)
- Ownership-based permissions (users can only manage their own notes)
- Dockerized for easy setup
- Clean code with pre-commit hooks (black, flake8, isort)

---

## 🛠️ Tech Stack

- Python 3.11+
- Django 4.x
- Django REST Framework
- Simple JWT
- PostgreSQL
- Docker & Docker Compose

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mammadov115/Notes-App.git
cd Notes-App
````

### 2. Setup `.env` file

Create a `.env` file based on `.env.example`.

```bash
cp .env.example .env
```

### 3. Build and Run with Docker

```bash
docker-compose up --build
```

App will be available at: `http://localhost:8000`

---

## 🔐 API Authentication

This project uses JWT for authentication.

* Register: `POST /users/register/`
* Login: `POST /users/token/`
* Logout: `POST /users/logout/` (blacklists the token)

Each authenticated request must include the access token:

```
Authorization: Bearer <your_token>
```

---

## 📘 API Endpoints

| Method | Endpoint            | Description             |
| ------ | ------------------- | ----------------------- |
| POST   | /users/register/    | Register new user       |
| POST   | /users/token/       | Obtain JWT tokens       |
| POST   | /users/logout/      | Blacklist refresh token |
| GET    | /notes/             | List all user notes     |
| POST   | /notes/             | Create a new note       |
| GET    | /notes/<id>/        | Get a specific note     |
| PUT    | /notes/<id>/        | Update a note           |
| DELETE | /notes/<id>/        | Delete a note           |

---

## 🧪 Running Tests

```bash
docker-compose exec web python manage.py test
```

Or, run a specific test file:

```bash
docker-compose exec web python manage.py test apps.notes.tests.test_views
```

---

## 🧹 Code Quality

This project uses:

* `black` for code formatting
* `isort` for import sorting
* `flake8` for linting
* `pre-commit` hooks

To run manually:

```bash
pre-commit run --all-files
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## 👤 Author

Made with ❤️ by [Mehman Mammadov](https://www.linkedin.com/in/mammadov1/)

