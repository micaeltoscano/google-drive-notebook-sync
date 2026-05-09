from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class FileSchema(BaseModel):

    id: Optional[int] = None

    title: str

    modified_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )