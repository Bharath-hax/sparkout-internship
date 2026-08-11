import re

from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator
)


# =========================================================
# PASSWORD VALIDATION
# =========================================================

def validate_password_strength(password: str) -> str:

    if len(password) < 8:
        raise ValueError(
            "Password must contain at least 8 characters"
        )

    if len(password) > 128:
        raise ValueError(
            "Password must not exceed 128 characters"
        )

    if not re.search(r"[A-Z]", password):
        raise ValueError(
            "Password must contain at least one uppercase letter"
        )

    if not re.search(r"[a-z]", password):
        raise ValueError(
            "Password must contain at least one lowercase letter"
        )

    if not re.search(r"[0-9]", password):
        raise ValueError(
            "Password must contain at least one number"
        )

    if not re.search(
        r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\]]",
        password
    ):
        raise ValueError(
            "Password must contain at least one special character"
        )

    return password


# =========================================================
# USER CREATE
# =========================================================

class UserCreate(BaseModel):

    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        max_length=128
    )


    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str):

        value = value.strip()

        if not re.fullmatch(
            r"[a-zA-Z0-9_]+",
            value
        ):
            raise ValueError(
                "Username can only contain letters, numbers and underscores"
            )

        return value


    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr):

        email = str(value).lower().strip()

        return email


    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str):

        return validate_password_strength(value)


# =========================================================
# USER RESPONSE
# =========================================================

class UserResponse(BaseModel):

    id: int

    username: str

    email: EmailStr

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# POST CREATE
# =========================================================

class PostCreate(BaseModel):

    title: str = Field(
        ...,
        min_length=3,
        max_length=200
    )

    content: str = Field(
        ...,
        min_length=1
    )

    category: str = Field(
        ...,
        min_length=2,
        max_length=100
    )


    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str):

        value = value.strip()

        if not value:
            raise ValueError(
                "Title cannot be empty"
            )

        return value


    @field_validator("content")
    @classmethod
    def validate_content(cls, value: str):

        value = value.strip()

        if not value:
            raise ValueError(
                "Content cannot be empty"
            )

        return value


    @field_validator("category")
    @classmethod
    def validate_category(cls, value: str):

        value = value.strip()

        if not value:
            raise ValueError(
                "Category cannot be empty"
            )

        return value


# =========================================================
# POST RESPONSE
# =========================================================

class PostResponse(BaseModel):

    id: int

    title: str

    content: str

    category: str

    author_id: int

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# NESTED USER PROFILE
# =========================================================

class UserProfileResponse(BaseModel):

    id: int

    username: str

    email: EmailStr

    created_at: datetime

    posts: list[PostResponse] = []

    model_config = ConfigDict(
        from_attributes=True
    )