---
name: 🐛 Bug report
about: Create a report to help us improve Chat Backend Service
title: '[BUG] '
labels: 'bug'
assignees: ''

---

## 📝 Description

Briefly describe the problem. What is going wrong with the REST API, WebSocket connection, or live demonstration client?

## 👣 How to Reproduce

Steps to reproduce the behavior:
1. Start the service (e.g., `docker compose up` or `python app/main.py`).
2. Make a request or connect via WebSocket (e.g., `POST /channels` or connect to `/ws/channels/1`).
3. Send the payload or action: '...' (e.g., send `{ "authorId": 1, "content": "" }`).
4. See error: '...' (e.g., unexpected status code, WebSocket crash, or invalid RFC 7807 response).

## 🎯 Expected Behavior

A clear and concise description of what you expected to happen (e.g., should return a 400 Bad Request with an RFC 7807 `application/problem+json` payload or send a WebSocket error frame).

## 📸 Screenshots or Execution Logs (if applicable)

Add screenshots, network tab captures, or log excerpts to help explain your problem.

## 💻 Environment

- **OS:** (e.g., Ubuntu 22.04, macOS Sonoma, Windows 11)
- **Execution Mode:** (e.g., Docker Compose, direct Docker container, or local Python virtual environment)
- **Python Version:** (e.g., 3.12.x)
- **Database:** (e.g., PostgreSQL 15 or in-memory SQLite for tests)
- **Client/Browser:** (if testing the `index.html` live demo, e.g., Chrome, Firefox, Postman, Insomnia)

## 🔍 Additional Context & Logs

Add any other context about the problem here. If the terminal or container logs showed an error traceback, please paste it here:

```text
[Paste your terminal output, Docker logs, or Python Traceback here]
```