# FastApi
from fastapi import APIRouter, Depends, status, Body
from fastapi.security import OAuth2PasswordRequestForm

from database.schemas import user_schema
from database.schemas.token_schema import Token
from ..services import auth_service
from ..services import user_service
from utils.db import get_db

router = APIRouter(
    prefix='/api/v1/auth',
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

    This path operation create new user in the app and save to database.

    Args:

        user (user_schema.User, optional): _description_. Defaults to Body(...).

    Returns:

        _type_: _description_
    """
    return user_service.create_user(user)


@router.post(
    path='/login/',
    status_code=status.HTTP_200_OK,
    response_model=Token,
    summary='Login a user'
)
# OAuth2PasswordRequestForm class depends whith the form data.
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login for access token

    This path operation login the user for access token.

    Args:

        form_data (OAuth2PasswordRequestForm): 
            - username: Ther user email.
            - password: The user password.

    Returns:

        json: json access token and token type.
    """

    access_token = auth_service.generate_token(
        form_data.username,
        form_data.password
    )
    return Token(access_token=access_token, token_type='bearer')
