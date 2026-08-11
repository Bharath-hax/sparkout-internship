from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Post, User
from ..schemas import (
    PostCreate,
    PostResponse
)


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# =========================================================
# CREATE POST
# =========================================================

@router.post(
    "/",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED
)
def create_post(
    post_data: PostCreate,
    author_id: int,
    db: Session = Depends(get_db)
):

    # -----------------------------------------------------
    # CHECK AUTHOR
    # -----------------------------------------------------

    author = (
        db.query(User)
        .filter(
            User.id == author_id
        )
        .first()
    )


    if author is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Author not found"
        )


    # -----------------------------------------------------
    # CREATE POST
    # -----------------------------------------------------

    post = Post(
        title=post_data.title,
        content=post_data.content,
        category=post_data.category,
        author_id=author_id
    )


    db.add(post)

    db.commit()

    db.refresh(post)


    return post


# =========================================================
# GET POST
# =========================================================

@router.get(
    "/{post_id}",
    response_model=PostResponse
)
def get_post(
    post_id: int,
    db: Session = Depends(get_db)
):

    post = (
        db.query(Post)
        .filter(
            Post.id == post_id
        )
        .first()
    )


    if post is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )


    return post