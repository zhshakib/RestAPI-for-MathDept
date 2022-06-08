from fastapi import APIRouter, status, HTTPException
from database import session
from models.Todo import TODO
from schema.Todo import Todo


router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)

# Geting the session


@router.get("/")
def read_todos():
    todos = session.query(TODO).all()
    session.close()
    return todos


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(todo: Todo):
    # making Todo Objects
    tododb = TODO(task=todo.task)
    # Add Todos to the Database
    session.add(tododb)
    session.commit()

    # Grabbing The id
    _id = tododb.id

    # Closing The session!
    session.close()

    return tododb


@router.get("/{id}")
def read_todo(id: int):
    todo = session.query(TODO).get(id)
    if not todo:
        raise HTTPException(
            status_code=404, detail=f"todo item with id {id} not found")
    return todo


@router.put("/{id}")
def update_todo(id: int, task: str):
    todo = session.query(TODO).get(id)
    if todo:
        todo.task = task
        session.commit()

    session.close()

    if not todo:
        raise HTTPException(
            status_code=404, detail=f"todo item with id {id} not found")
    return todo


@router.delete("/{id}")
def delete_todo(id: int):
    todo = session.query(TODO).get(id)
    if todo:
        session.delete(todo)
        session.commit()
        session.close()
    return f"delete todo item with id {id}"
