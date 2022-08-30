from fastapi import APIRouter, status

users = APIRouter(
    prefix='/users',
    tags=['User'],
)


@users.get(
    path='/',
    status_code=status.HTTP_200_OK,
    summary='Hello User'
)
async def user():
    return {'user': 'ok'}
