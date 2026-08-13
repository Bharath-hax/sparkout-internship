from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models, schemas, crud


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Todo API",
    description="FastAPI + SQLAlchemy Todo Application",
    version="1.0.0"
)


# =====================================================
# USER ROUTES
# =====================================================

@app.post(
    "/users",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user_data: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(db, user_data)


@app.get(
    "/users",
    response_model=list[schemas.UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):
    return crud.get_users(db)


@app.get(
    "/users/{user_id}",
    response_model=schemas.UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@app.put(
    "/users/{user_id}",
    response_model=schemas.UserResponse
)
def update_user(
    user_id: int,
    user_data: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    user = crud.update_user(
        db,
        user_id,
        user_data
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@app.delete(
    "/users/{user_id}"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = crud.delete_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }


# =====================================================
# TASK ROUTES
# =====================================================

@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task_data: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    # Check whether the user exists
    user = crud.get_user(db, task_data.user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return crud.create_task(db, task_data)


@app.get(
    "/tasks",
    response_model=list[schemas.TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db)
):
    return crud.get_tasks(db)


@app.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = crud.get_task(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.get(
    "/users/{user_id}/tasks",
    response_model=list[schemas.TaskResponse]
)
def get_user_tasks(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return crud.get_user_tasks(db, user_id)


@app.put(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def update_task(
    task_id: int,
    task_data: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):
    task = crud.update_task(
        db,
        task_id,
        task_data
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.delete(
    "/tasks/{task_id}"
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = crud.delete_task(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }