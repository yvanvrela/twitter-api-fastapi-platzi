from fastapi import FastAPI
from routes.home_route import route as home
from routes.user_route import users
from routes.tweet_route import tweets


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
