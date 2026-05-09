from datetime import datetime

from core.configs import settings

from sqlalchemy import Column, Integer, String, DateTime

class Files(settings.DBBaseModel):

    __tablename__ = 'Computacional_Intelligence_Notebooks'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(100))
    modified_at: datetime = Column(DateTime)

