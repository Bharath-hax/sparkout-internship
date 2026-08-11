from math import ceil

from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    Query,
    status
)
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Comment, Post
from .schemas import (
    CommentCreate,
    CommentResponse,
    PaginationMeta,
    PostCreate,
    PostListResponse,
    PostResponse
)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Blog API",
    description="Blog API with posts, comments, filtering and pagination",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Blog API is running",
        "version": "1.0.0"
    }


@app.post(
    "/posts",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED
)
def create_post(
    post_data: PostCreate,
    db: Session = Depends(get_db)
):
    post = Post(
        title=post_data.title,
        content=post_data.content,
        category=post_data.category,
        author=post_data.author
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


@app.get(
    "/posts",
    response_model=PostListResponse
)
def get_posts(
    category: str | None = Query(
        default=None,
        description="Filter posts by category"
    ),
    page: int = Query(
        default=1,
        ge=1,
        description="Page number"
    ),
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Posts per page"
    ),
    db: Session = Depends(get_db)
):
    query = db.query(Post)

    if category:
        query = query.filter(
            Post.category == category
        )

    total = query.count()

    offset = (page - 1) * limit

    posts = (
        query
        .order_by(Post.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )

    total_pages = (
        ceil(total / limit)
        if total > 0
        else 0
    )

    return PostListResponse(
        posts=posts,
        pagination=PaginationMeta(
            page=page,
            limit=limit,
            total=total,
            total_pages=total_pages,
            has_next=page < total_pages,
            has_previous=page > 1
        )
    )


@app.get(
    "/posts/{post_id}",
    response_model=PostResponse
)
def get_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    post = (
        db.query(Post)
        .filter(Post.id == post_id)
        .first()
    )

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )

    return post


@app.post(
    "/posts/{post_id}/comments",
    response_model=CommentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_comment(
    post_id: int,
    comment_data: CommentCreate,
    db: Session = Depends(get_db)
):
    post = (
        db.query(Post)
        .filter(Post.id == post_id)
        .first()
    )

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )

    comment = Comment(
        post_id=post_id,
        author=comment_data.author,
        content=comment_data.content
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


@app.get(
    "/posts/{post_id}/comments",
    response_model=list[CommentResponse]
)
def get_comments(
    post_id: int,
    db: Session = Depends(get_db)
):
    post = (
        db.query(Post)
        .filter(Post.id == post_id)
        .first()
    )

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )

    comments = (
        db.query(Comment)
        .filter(Comment.post_id == post_id)
        .order_by(Comment.created_at.asc())
        .all()
    )

    return comments
