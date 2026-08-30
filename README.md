# 🚀 Chat Backend Service

![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-8.1+-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

A minimal real-time chat backend service built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **WebSockets**. The service provides a REST API to create and manage channels, retrieve message history, and exposes a WebSocket endpoint per channel to broadcast messages and edits in real time. It also includes a zero-dependency HTML live demonstration page.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Tech Stack & Prerequisites](#-tech-stack--prerequisites)
- [Repository Structure](#-repository-structure)
- [Environment Variables](#-environment-variables)
- [Getting Started & Execution](#-getting-started--execution)
  - [Option A: Running with Docker Compose](#option-a-running-with-docker-compose-recommended)
  - [Option B: Running DB and Service Independently](#option-b-running-db-and-service-independently)
  - [Option C: Running Locally for Development](#option-c-running-locally-for-development)
- [Live Demo Instructions](#-live-demo-instructions)
- [Running Tests](#-running-tests)
- [Error Handling (RFC 7807)](#-error-handling-rfc-7807)

---

## 📋 Overview

The Chat Backend Service is designed around two main communication models:
1. **REST API**: Handles channel management (`POST /channels`, `GET /channels`) and message history retrieval (`GET /channels/{channelId}/messages`).
2. **WebSocket Connection**: Real-time communication for sending (`SEND_MESSAGE`) and updating (`EDIT_MESSAGE`) messages, automatically broadcasting state changes to all connected clients in a channel.

All error responses strictly follow the **RFC 7807** standard using the `application/problem+json` content type.

---

## 🛠️ Tech Stack & Prerequisites

### Tech Stack
* **Language**: Python 3.12
* **Framework**: FastAPI
* **ASGI Server**: Uvicorn
* **ORM & Database**: SQLAlchemy 2.0 & PostgreSQL 15
* **Testing Library**: [pytest User Guide](https://docs.pytest.org/)
* **Containerization**: Docker & Docker Compose

### Prerequisites
* [Docker Engine](https://docs.docker.com/get-docker/) `20.10+` and [Docker Compose](https://docs.docker.com/compose/) `2.0+`
* *(Optional)* Python `3.12+` if running outside containers locally.

---

## 🏗️ Repository Structure

```text
chat-backend-service/
├── app/
│   ├── controllers/         # API Routers (REST & WebSockets)
│   ├── exceptions/          # RFC 7807 Exception handling
│   ├── models/              # SQLAlchemy Database Models
│   ├── repositories/        # Database access layer
│   ├── schemas/             # Pydantic Schemas / DTOs
│   ├── services/            # Core business logic
│   ├── websockets/          # Connection manager for real-time channels
│   ├── config.py            # Environment settings management
│   ├── database.py          # Database setup and sessions
│   └── main.py              # Application entry point
├── public/
│   └── index.html           # Minimal HTML WebSocket live demonstration client
├── test/
│   ├── conftest.py          # Pytest fixtures and SQLite setup
│   ├── test_channels.py     # REST Channel integration tests
│   ├── test_messages.py     # REST Message integration tests
│   └── test_websockets.py   # WebSocket communication tests
├── compose.yaml             # Docker Compose orchestration
├── Dockerfile               # Container spec
├── pytest.ini               # Pytest configuration
└── requirements.txt         # Project Python dependencies
```

---

## ⚙️ Environment Variables

The application is fully configurable via environment variables. Default values are provided for quick development.

| Variable | Description | Default |
| :--- | :--- | :--- |
| `ENVIRONMENT` | Execution environment (`development`, `testing`, `production`) | `development` |
| `HOST` | Server host address | `0.0.0.0` |
| `PORT` | Server listening port | `8080` |
| `DATABASE_HOST` | Database server host | `localhost` (`db` inside Docker) |
| `DATABASE_PORT` | Database server port | `5432` |
| `DATABASE_NAME` | Database name| `db` |
| `DATABASE_USER` | Database user | `admin` |
| `DATABASE_PASSWORD` | Database user password| `password` |

---

## 🚀 Getting Started & Execution

### Option A: Running with Docker Compose (Recommended)

To spin up both the **PostgreSQL database** and the **Chat Backend Service** together in a unified network:

```bash
docker compose up --build
```

The backend service will be available at `http://localhost:8080`.

---

### Option B: Running DB and Service Independently

1. **Create Docker Network**:
   ```bash
   docker network create chat-network
   ```

2. **Run PostgreSQL Container**:
   ```bash
   docker run -d \
     --name chat_db \
     --network chat-network \
     -p 5432:5432 \
     -e POSTGRES_USER=admin \
     -e POSTGRES_PASSWORD=password \
     -e POSTGRES_DB=db \
     postgres:15-alpine
   ```

3. **Build Backend Docker Image**:
   ```bash
   docker build -t chat-backend-service .
   ```

4. **Run Backend Service Container**:
   ```bash
   docker run -d \
     --name chat_service \
     --network chat-network \
     -p 8080:8080 \
     -e DATABASE_HOST=chat_db \
     -e DATABASE_PORT=5432 \
     -e DATABASE_USER=admin \
     -e DATABASE_PASSWORD=password \
     -e DATABASE_NAME=db \
     chat-backend-service
   ```

---

### Option C: Running Locally for Development

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Ensure PostgreSQL is Running**, then run:
   ```bash
   python app/main.py
   ```

---

## 🌐 Live Demo Instructions

A minimal, framework-free HTML demonstration client is bundled in the service.

1. Ensure the backend application is running.
2. Open your browser and navigate to:
   ```text
   http://localhost:8080
   ```
3. **Usage**:
   - Create a channel using the sidebar input.
   - Select the channel to automatically connect to its WebSocket endpoint (`/ws/channels/{channelId}`).
   - Send and edit messages in real-time across multiple open browser tabs to verify broadcasting.

---

## 🧪 Running Tests

The test suite uses **pytest** with an in-memory SQLite database to run integration tests without external database dependencies.

To execute all tests:

```bash
pytest
```

To run tests with detailed verbosity:

```bash
pytest -v
```

---

## ⚠️ Error Handling (RFC 7807)

API error responses comply with the **RFC 7807** Problem Details standard and set `Content-Type: application/problem+json`.

**Example 404 Response**:
```json
{
  "type": "about:blank",
  "title": "Channel Not Found",
  "status": 404,
  "detail": "The channel with ID 999 was not found.",
  "instance": "/channels/999/messages"
}
```
