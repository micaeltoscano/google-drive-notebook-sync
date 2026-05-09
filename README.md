# Computational Intelligence Sync

Backend automation service built with FastAPI, SQLAlchemy, and PostgreSQL to synchronize and manage Computational Intelligence lecture notebooks from Google Drive automatically.

---

## How to Use

### Prerequisites

- Docker and Docker Compose installed
- A Google Cloud project with the Drive API enabled
- `credentials.json` from Google OAuth2 (place it in the project root)

### 1. Clone the repository

```bash
git clone https://github.com/micaeltoscano/google-drive-notebook-sync.git
cd google-drive-notebook-sync
```

### 2. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@postgres:5432/google_drive_project
```

### 3. Authenticate with Google Drive

Before running the project, generate your `token.json` by running the auth service once locally:

```bash
python -m services.drive_auth_service
```

A browser window will open for you to authorize access. A `token.json` file will be created in the project root.

### 4. Start the containers

```bash
docker-compose up --build -d
```

### 5. Create the database tables

```bash
docker exec fastapi_app python -m schemas.create_tables
```

### 6. Access the API

Open your browser at `http://localhost:8000/docs` to access the interactive Swagger UI.

### 7. Sync notebooks from Google Drive

In the Swagger UI, call `POST /api/v1/notebooks/sync`. This will fetch all `.ipynb` files from the configured Drive folder, download them to the `notebooks/` directory, and save their metadata to the database.

### 8. List synced notebooks

Call `GET /api/v1/notebooks` to see all notebooks stored in the database.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/notebooks` | List all synced notebooks |
| POST | `/api/v1/notebooks` | Manually add a notebook |
| DELETE | `/api/v1/notebooks/{id}` | Delete a notebook by ID |
| POST | `/api/v1/notebooks/sync` | Sync notebooks from Google Drive |

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- AsyncPG
- Pydantic v2
- Uvicorn
- Docker

---

## Project Structure

```text
google-drive-notebook-sync/
│
├── api/
│   └── v1/
│       └── endpoints/
│           └── notebooks.py
│
├── core/
│   ├── configs.py
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
├── services/
│   ├── drive_auth_service.py
│   └── sync_services.py
│
├── notebooks/
├── .env
├── credentials.json
├── token.json
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Features

- Google Drive integration with OAuth2 authentication
- Automatic notebook synchronization with duplicate detection
- Async backend architecture
- PostgreSQL database for metadata persistence
- REST API with FastAPI and interactive Swagger docs
- SQLAlchemy async ORM
- Docker support