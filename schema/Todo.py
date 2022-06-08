from pydantic import BaseModel

# Create ToDoRequest Base Model


class Todo(BaseModel):
    task: str
