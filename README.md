# Computational Intelligence Sync

🚧 Project currently under development.

Backend automation service built with FastAPI, SQLAlchemy, and PostgreSQL to synchronize and manage Computational Intelligence lecture notebooks from Google Drive automatically.

The main goal of this project is to automate the process of monitoring, collecting, and storing lecture notebooks uploaded to Google Drive while exploring modern backend architecture and AI automation workflows.

---

## Current Status

The project is currently in the initial backend development phase.

### Implemented

- FastAPI project structure
- PostgreSQL integration
- Async SQLAlchemy setup
- Database session dependency injection
- Pydantic schemas
- Environment variable configuration
- Table creation scripts
- ORM models
- Docker support

### In Progress

- Google Drive API integration
- Automatic notebook synchronization
- File metadata persistence
- REST API endpoints

### Planned Features

- Background synchronization tasks
- Duplicate file detection
- Automatic update tracking
- Notebook version control
- AI-powered notebook analysis
- Authentication system
- Deployment pipeline

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
Fast-API-classes/
│
├── core/
│   └── configs.py
│
├── database/
│   ├── database.py
│   └── deps.py
│
├── models/
│   ├── model.py
│   └── _all_models.py
│
├── schemas/
│   ├── schemas.py
│   └── create_tables.py
│
├── api/
│
├── .env
├── requirements.txt
└── README.md