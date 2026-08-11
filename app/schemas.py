from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


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

    author: str = Field(
        ...,
        min_length=2,
        max_length=100
    )


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    author: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class CommentCreate(BaseModel):
    author: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    content: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )


class CommentResponse(BaseModel):
    id: int
    post_id: int
    author: str
    content: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class PaginationMeta(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int
    has_next: bool
    has_previous: bool


class PostListResponse(BaseModel):
    posts: list[PostResponse]
    pagination: PaginationMeta
