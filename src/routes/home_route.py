from fastapi import APIRouter


home = APIRouter(
    prefix='/',
    tags=['home'],
)


@home.get(path='/', tags=['Home'], summary='Home in the app')
async def home():
    """Home

    Returns:

        json: json hello twitter
    """
    return {'Twitter': True}
