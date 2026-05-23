from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database.connection import SessionLocal,get_db
from models.todo_model import Todo
from schemas.todo_schema import TodoCreate
from auth import get_current_user

router = APIRouter(tags=["TODO"])

# GET TODOS
@router.get("/todos")
def get_todos(db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
    todos = db.query(Todo).filter(Todo.owner_email == current_user).all()
    return todos


# CREATE TODO
@router.post("/todos")
def create_todo(todo: TodoCreate,db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
    new_todo = Todo(task=todo.task,description=todo.description,owner_email=current_user)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# DELETE TODO
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int,db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
    todo = db.query(Todo).filter(Todo.id == todo_id,Todo.owner_email == current_user).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    db.delete(todo)
    db.commit()
    return {
        "message": "Deleted"
    }


# TOGGLE TODO
@router.put("/todos/{todo_id}")
def toggle_todo(todo_id: int,db:Session=Depends(get_db),current_user: str = Depends(get_current_user)):
    db = SessionLocal()
    todo = db.query(Todo).filter(Todo.id == todo_id,Todo.owner_email == current_user).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    todo.completed = not todo.completed
    db.commit()
    db.refresh(todo)
    return todo