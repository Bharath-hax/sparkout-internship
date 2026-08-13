from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models
from .schemas import (
    UserCreate,
    UserUpdate,
    TaskCreate,
    TaskUpdate
)


# =====================================================
# USER CRUD
# =====================================================

def create_user(
    db: Session,
    user_data: UserCreate
):
    user = models.User(
        username=user_data.username,
        email=user_data.email
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_users(db: Session):
    statement = select(models.User)

    result = db.execute(statement)

    return result.scalars().all()


def get_user(
    db: Session,
    user_id: int
):
    return db.get(models.User, user_id)


def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate
):
    user = db.get(models.User, user_id)

    if user is None:
        return None

    if user_data.username is not None:
        user.username = user_data.username

    if user_data.email is not None:
        user.email = user_data.email

    db.commit()
    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user_id: int
):
    user = db.get(models.User, user_id)

    if user is None:
        return None

    db.delete(user)
    db.commit()

    return user


# =====================================================
# TASK CRUD
# =====================================================

def create_task(
    db: Session,
    task_data: TaskCreate
):
    task = models.Task(
        title=task_data.title,
        description=task_data.description,
        user_id=task_data.user_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_tasks(db: Session):
    statement = select(models.Task)

    result = db.execute(statement)

    return result.scalars().all()


def get_task(
    db: Session,
    task_id: int
):
    return db.get(models.Task, task_id)


def get_user_tasks(
    db: Session,
    user_id: int
):
    statement = (
        select(models.Task)
        .where(models.Task.user_id == user_id)
    )

    result = db.execute(statement)

    return result.scalars().all()


def update_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate
):
    task = db.get(models.Task, task_id)

    if task is None:
        return None

    if task_data.title is not None:
        task.title = task_data.title

    if task_data.description is not None:
        task.description = task_data.description

    if task_data.completed is not None:
        task.completed = task_data.completed

    db.commit()
    db.refresh(task)

    return task


def delete_task(
    db: Session,
    task_id: int
):
    task = db.get(models.Task, task_id)

    if task is None:
        return None

    db.delete(task)
    db.commit()

    return task