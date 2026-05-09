from fastapi import FastAPI

import uvicorn

from api.v1.endpoints import notebooks
from core.configs import settings

app = FastAPI(title='Notebook Sync API')
app.include_router(notebooks.router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")