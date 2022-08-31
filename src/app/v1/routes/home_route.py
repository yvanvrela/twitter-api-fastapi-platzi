from fastapi import APIRouter


route = APIRouter(
    prefix='/home',
    tags=['Home'],
)


@route.get(path='/', tags=['Home'], summary='Home in the app')
async def home():
    """Home

    Returns: 

        json: json hello twitter
    """
    return {'Twitter': True}
