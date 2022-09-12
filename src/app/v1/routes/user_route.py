from typing import List

# FastApi
from fastapi import APIRouter, Depends, Path, Body, Response, status
from app.v1.services.auth_service import get_current_user

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


@router.put(
    path='/{id}',
    status_code=status.HTTP_200_OK,
    response_model=user_schema.UserOut,
    dependencies=[Depends(get_db)],
    summary='Update a user',
)
async def update_user(
    id: int = Path(
        ...,
        gt=0,
        example=1,
    ),
    user: user_schema.UserLogin = Body(...),
    current_user=Depends(get_current_user)
):
    return user_service.update_user(id, user, current_user)


@router.delete(
    path='/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_db)],
    summary='Delete a user',
)
async def delete_user(
    id: int = Path(
        ...,
        gt=0,
        example=1,
    ),
    current_user=Depends(get_current_user),
):
    """Delete a user

    This path operation delete a user in the database.

    Args:

        id (int): This is the user id.
        token (str): This is the token user.

    Returns:

        status_code: 204
    """
    user_service.delete_user(id, current_user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
