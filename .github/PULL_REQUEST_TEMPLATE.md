# 🚀 Pull Request

## 📝 Description

Briefly describe your changes:
- What REST endpoint, WebSocket logic, database model, or repository layer did you implement or update?
- How does this improve the backend performance, concurrency handling, or overall API design?

### 📸 Screenshots or Execution Logs (Optional)
*If you added a new WebSocket behavior, changed the live demo page (`index.html`), or ran manual testing, attach a screenshot, log excerpt, or short GIF here.*

---

## 🏗️ Type of Change
Please check the option that is relevant:
- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds REST/WebSocket functionality)
- [ ] ♻️ Code refactor (improving architecture, schemas, or service layer without changing API contract)
- [ ] 🧪 Tests (adding missing unit, integration, or WebSocket tests)
- [ ] 🐳 Docker / Infrastructure update (changes to `Dockerfile`, `compose.yaml`, or env configs)
- [ ] 📝 Documentation update (updates to `README.md` or `CONTRIBUTING.md`)

---

## ✅ Checklist

- [ ] My code runs locally and the backend starts without errors (`python app/main.py` or Docker).
- [ ] All unit and integration tests pass successfully (`pytest`).
- [ ] Error responses maintain strict compliance with **RFC 7807** (`application/problem+json`).
- [ ] I have followed the layered architectural structure (`controllers`, `services`, `repositories`, `schemas`, `models`).
- [ ] I have updated the `README.md` or environment settings if I added new configuration options.

---

Thanks for your contribution to **Chat Backend Service**! 🎉