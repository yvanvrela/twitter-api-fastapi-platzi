from fastapi import FastAPI
from app.v1.routes.home_route import route as home
from app.v1.routes.user_route import router as users
from app.v1.routes.tweet_route import router as tweets


def create_app() -> FastAPI:
    """Create FastApi

    Create a new FastApi instance, and apply the configurations

    Returns:

        FastAPI: a fastapi app
    """
    app = FastAPI()

    app.include_router(home)
    app.include_router(users)
    app.include_router(tweets)

    return app
