from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    id: int
    author: str
    content: str
    timestamp: datetime = datetime.now()