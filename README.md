# 🛡️ Token Service - Django + FastAPI Style 

A simple backend token issuing service with async support, built using Django REST Framework.

---

## 🚀 Features

- Asynchronous token issuing
- Credentials validation
- Simulated JWT-like token responses
- Testable, modular architecture

---

## 📁 Project Structure

```
token_service/
│
├── schemas/
│   └── models.py                  # Pydantic-like schemas
│
├── services/
│   ├── auth_service.py           # Login/authentication logic
│   ├── token_service.py          # Simulated token generation
│   └── orchestrator_service.py   # Orchestrates authentication and token issuing
│
├── views/
│   └── request_token_view.py     # Django REST view for the /api/request-token endpoint
│
├── tests/
│   ├── test_auth_service.py
│   ├── test_token_service.py
│   └── test_orchestrator_service.py
│
├── __init__.py
├── urls.py
├── settings.py
├── wsgi.py
├── asgi.py
└── manage.py
```

---

## 🧰 Tech Stack

- Python 3.11
- Django 5.2
- Django REST Framework
- Async functions for service logic
- Pytest + pytest-asyncio for unit testing
- Docker support for easy deployment

---

## 🔧 Installation (Development)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/token-service.git
cd token-service

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the development server
python manage.py runserver
```

---

## 🐳 Docker Setup

```bash
# Build the Docker image
docker build -t token-service .

# Run the container
docker run -p 8000:8000 token-service
```

---

## 🧪 Running Tests

```bash
# Run all unit tests
pytest token_service/tests/
```

### Sample Test Output

- ✅ test_authenticate_success
- ✅ test_generate_token_success
- ❌ test_generate_token_failure for "A" usernames

---

## 📬 API Endpoint

### POST `/api/request-token/`

**Request Body**:

```json
{
  "username": "user123",
  "password": "USER123"
}
```

**Success Response**:

```json
{
  "token": "user123_1714200000"
}
```

**Failure Response** (wrong password):

```json
{
  "detail": "Invalid credentials"
}
```

---

## 🔒 Credentials & Token Rules

- Password must equal `username.upper()`
- Users with usernames starting with `A` cannot be issued tokens
- Tokens are returned as `{username}_{timestamp}`

---

## 📦 Dockerfile (inside repo)

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

## 📝 License

MIT License. Use freely for learning and projects.

---

## 🤝 Contributions

Pull requests, issues, and suggestions are welcome!