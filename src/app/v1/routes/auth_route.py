# FastApi
from fastapi import APIRouter, Depends, status, Body
from fastapi.security import OAuth2PasswordRequestForm

from database.schemas import user_schema
from database.schemas.token_schema import Token
from ..services import auth_service
from ..services import user_service
from utils.db import get_db

router = APIRouter(
    prefix='/auth',
    tags=['Auth', 'Users'],
)


# Endpoints

@router.post(
    path='/signup/',
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.UserBase,
    dependencies=[Depends(get_db)],
    summary='Create a new user'
)
async def signup_user(user: user_schema.UserLogin = Body(...)):
    """Create a new user

    This endpoint create new user in the app and save to database.

    Args:

        user (user_schema.User, optional): _description_. Defaults to Body(...).

    Returns:

        _type_: _description_
    """
    return user_service.create_user(user)
