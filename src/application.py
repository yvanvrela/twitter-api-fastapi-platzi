from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create FastApi

    Returns:

        FastAPI: a fastapi app
    """
    app = FastAPI()

    return app
