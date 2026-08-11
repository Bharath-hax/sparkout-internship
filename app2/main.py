from fastapi import FastAPI

from .database import Base, engine

from .routers import users, posts


# =========================================================
# DATABASE
# =========================================================

Base.metadata.create_all(
    bind=engine
)


# =========================================================
# APPLICATION
# =========================================================

app = FastAPI(
    title="Blog API",
    description="FastAPI Blog API with Users, Posts and Nested Profiles",
    version="1.0.0"
)


# =========================================================
# ROUTERS
# =========================================================

app.include_router(
    users.router
)

app.include_router(
    posts.router
)


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():

    return {
        "message": "Blog API is running",
        "version": "1.0.0"
    }