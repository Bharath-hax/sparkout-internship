from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from passlib.context import CryptContext

from sqlalchemy.orm import Session, selectinload

from ..database import get_db
from ..models import User
from ..schemas import (
    UserCreate,
    UserProfileResponse,
    UserResponse
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# =========================================================
# PASSWORD HASHING
# =========================================================

def hash_password(password: str) -> str:

    return pwd_context.hash(password)


# =========================================================
# CREATE USER
# =========================================================

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    # -----------------------------------------------------
    # CHECK USERNAME
    # -----------------------------------------------------

    existing_username = (
        db.query(User)
        .filter(
            User.username == user_data.username
        )
        .first()
    )

    if existing_username:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists"
        )


    # -----------------------------------------------------
    # CHECK EMAIL
    # -----------------------------------------------------

    existing_email = (
        db.query(User)
        .filter(
            User.email == str(user_data.email)
        )
        .first()
    )

    if existing_email:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )


    # -----------------------------------------------------
    # HASH PASSWORD
    # -----------------------------------------------------

    password_hash = hash_password(
        user_data.password
    )


    # -----------------------------------------------------
    # CREATE USER
    # -----------------------------------------------------

    user = User(
        username=user_data.username,
        email=str(user_data.email),
        password_hash=password_hash
    )


    db.add(user)

    db.commit()

    db.refresh(user)


    return user


# =========================================================
# GET USER
# =========================================================

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.id == user_id
        )
        .first()
    )


    if user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


    return user


# =========================================================
# GET USER PROFILE WITH POSTS
# =========================================================

@router.get(
    "/{user_id}/profile",
    response_model=UserProfileResponse
)
def get_user_profile(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .options(
            selectinload(User.posts)
        )
        .filter(
            User.id == user_id
        )
        .first()
    )


    if user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


    return user