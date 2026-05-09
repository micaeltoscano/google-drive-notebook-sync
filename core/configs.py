from typing import ClassVar

from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str

    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()