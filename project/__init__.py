from fastapi import FastAPI

from project.celery_utils import create_celery


def create_app() -> FastAPI:
    app = FastAPI()

    # do this before loading routes
    # singleton and factory?
    app.celery_app = create_celery()  # type: ignore

    from project.users import users_router

    app.include_router(users_router)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app
