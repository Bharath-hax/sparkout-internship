from pydantic import BaseModel, ConfigDict


# -------------------------
# User Schemas
# -------------------------

class UserCreate(BaseModel):
    username: str
    email: str


class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


# -------------------------
# Task Schemas
# -------------------------

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    user_id: int


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    user_id: int

    model_config = ConfigDict(from_attributes=True)