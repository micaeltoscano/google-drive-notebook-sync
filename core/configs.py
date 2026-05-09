from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings): 

#BaseSettings is used to read environment variables, validate confs, centralize application settings
    
    API_V1_STR: str = '/api/v1'
    DATABASE_URL: str
    DBBaseModel = declarative_base()

    class Config:

        case_sensitive = True
        env_file = ".env"

settings = Settings()