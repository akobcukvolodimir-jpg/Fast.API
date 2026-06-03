from pydantic import BaseModel


class Task(BaseModel):
    id: int = 0
    title: str
    completed: bool = False