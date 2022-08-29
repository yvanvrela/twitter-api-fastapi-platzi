from application import create_app
import uvicorn

app = create_app()




@app.get(path='/', tags=['Home'], summary='Home in the app')
async def home():
    """Home

    Returns:

        json: json hello twitter
    """
    return {'Twitter': True}


def main() -> None:
    """Run App
    """
    uvicorn.run(
        app='main:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )


if __name__ == '__main__':
    main()
