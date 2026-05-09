# Computational Intelligence Sync

Backend automation service built with FastAPI, SQLAlchemy, and PostgreSQL to synchronize and manage Computational Intelligence lecture notebooks from Google Drive automatically.

---

## Features

- Google Drive integration
- Automatic notebook synchronization
- Async backend architecture
- PostgreSQL database integration
- REST API with FastAPI
- SQLAlchemy async ORM
- Environment variable configuration
- Modular project structure

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- AsyncPG
- Pydantic v2
- Uvicorn

---

## Project Structure

```text
app/
├── core/
│   └── configs.py
│
├── database/
│   ├── database.py
│   └── deps.py
│
├── models/
│   └── file_model.py
│
├── schemas/
│   └── file_schema.py
│
├── main.py
│
└── .env

