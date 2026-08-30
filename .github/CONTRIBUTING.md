# 🤝 Contributing to Chat Backend Service

Thank you for your interest in contributing to the **Chat Backend Service**! This project is designed as an event-driven, real-time chat service powered by FastAPI, WebSockets, PostgreSQL, and Docker. Whether you are fixing a bug, adding new features, improving documentation, or refining tests, your contributions are highly appreciated!

---

## 📑 Table of Contents

- [How to Contribute](#-how-to-contribute)
- [Development Setup](#-development-setup)
- [Coding Standards & Conventions](#-coding-standards--conventions)
- [Testing Guidelines](#-testing-guidelines)
- [Ideas for Contribution](#-ideas-for-contribution)

---

## 🚀 How to Contribute

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/[YOUR_GITHUB_USERNAME]/chat-backend-service.git
   cd chat-backend-service
   ```
3. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/my-new-feature
   ```
4. **Make Your Changes**: Implement your changes following our coding and testing standards.
5. **Commit Your Changes**: Use clear and descriptive commit messages (following [Conventional Commits](https://www.conventionalcommits.org/)):
   ```bash
   git commit -m "feat(websocket): add heartbeats and reconnection events"
   ```
6. **Push to Your Branch**:
   ```bash
   git push origin feature/my-new-feature
   ```
7. **Open a Pull Request**: Describe your changes in detail and link any related issues.

---

## 🛠️ Development Setup

To get your development environment running locally:

1. **Spin up PostgreSQL via Docker Compose**:
   ```bash
   docker compose up -d db
   ```

2. **Set up a Python Virtual Environment**:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Application in Development Mode**:
   ```bash
   python app/main.py
   ```
   The app will run at `http://localhost:8080`.

---

## 📐 Coding Standards & Conventions

To maintain project consistency and code quality, please follow these guidelines:

- **Layered Architecture**: Respect the separation of concerns:
  - `controllers/`: Handles HTTP REST routes and WebSocket connection routing.
  - `services/`: Contains business logic and orchestrates validation.
  - `repositories/`: Encapsulates database queries using SQLAlchemy.
  - `schemas/`: Pydantic models for data validation and RFC 7807 error structures.
  - `models/`: SQLAlchemy ORM entity models.
- **RFC 7807 Compliance**: Ensure all REST API errors raise `HTTPExceptionRFC7807` so they are formatted as `application/problem+json`.
- **WebSocket Error Frames**: Errors encountered over WebSocket connections should return lightweight JSON error messages without closing the connection unnecessarily.
- **Type Hints**: Always use explicit Python type annotations.
- **Language**: All code, comments, commit messages, and documentation must be written in **English**.

---

## 🧪 Testing Guidelines

Every pull request must pass all tests before merging. We use **pytest** with an isolated SQLite in-memory database.

1. **Run All Tests**:
   ```bash
   pytest
   ```

2. **Writing Tests**:
   - Add unit or integration tests under the `test/` directory for any new REST endpoints or WebSocket actions.
   - Refer to the [pytest Documentation](https://docs.pytest.org/) for test patterns and fixtures.

---

## 💡 Ideas for Contribution

Looking for inspiration on where to start? Here are a few valuable areas for enhancement:

- 🔒 **Authentication & Authorization**: Implement JWT or token-based authentication for WebSocket handshakes and REST routes.
- 📡 **Redis Pub/Sub Scaling**: Refactor `ConnectionManager` to support horizontal scaling across multiple container instances using Redis.
- 💬 **Message Pagination**: Add cursor-based pagination to `GET /channels/{channelId}/messages`.
- 🔌 **Heartbeats / Ping-Pong**: Implement ping-pong frames in WebSocket handling to drop stale connections cleanly.
- 🤖 **CI/CD Pipeline**: Add a GitHub Actions workflow to run `pytest` automatically on PRs.

Thank you for helping make this project better! 🎉