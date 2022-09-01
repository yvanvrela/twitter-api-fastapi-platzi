# FastApi
from application import create_app
from database.scripts.create_tables import create_tables
import uvicorn

app = create_app()


def main() -> None:
    """Run App
    """
    create_tables()
    uvicorn.run(
        app='main:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )


if __name__ == '__main__':
    main()
