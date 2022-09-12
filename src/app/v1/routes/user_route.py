from typing import List

# FastApi
from fastapi import APIRouter, Depends, Path, Body, status

from database.schemas import user_schema
from ..services import user_service
from utils.db import get_db


router = APIRouter(
    prefix='/api/v1/users',
    tags=['Users'],
)


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_model=List[user_schema.UserOut],
    dependencies=[Depends(get_db)],
    summary='Get all users',
)
async def get_users():
    return user_service.get_users()


@router.get(
    path='/{id}',
    status_code=status.HTTP_200_OK,
    response_model=user_schema.UserOut,
    dependencies=[Depends(get_db)],
    summary='Get a user',
)
async def get_user(
    id: int = Path(
        ...,
        gt=0,
        example=1,
    ),
):
    """Get a user

    This path operation show a user by id in the app.

    Args:

        id (int): This is the user id.

    Returns:

        json: json user information.
    """
    return user_service.get_user_by_id(id)
