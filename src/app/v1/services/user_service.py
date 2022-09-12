from typing import List

# FastApi
from fastapi import HTTPException, status

# Utils
from utils import passwords

# Models and Schemas
from database.models.user_model import User as UserModel
from database.schemas import user_schema


def create_user(user: user_schema.UserLogin) -> dict:
    """Create a user 

    This is functions created a user in the database.

    Args:

        user (user_schema.UserLogin): This is a User model content: email, first name, last name, birth date and password.

    Raises:

        HTTPException: code:401, message: Email already registered.

    Returns:

        dict: return a User schema whith the all informations.
    """

    # Find if exist a user
    user_reference = get_user(user_email=user.email)

    if user_reference:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email already registered'
        )

    # Initialize the data to the user model
    db_user = UserModel(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        birth_date=user.birth_date,
        password=passwords.hash_password(user.password)
    )

    # Save a data in the database
    db_user.save()

    return user_schema.UserBase(
        user_id=db_user.id,
        first_name=db_user.first_name,
        last_name=user.last_name,
        email=user.email,
        birth_date=user.birth_date,
    )


def get_user(user_email: str) -> UserModel.email:
    """Get user by database

    Filter a user email in database

    Args:

        user_email (str): This is the user email.

    Returns: 

        UserModel: UserModel is a object user.
    """
    return UserModel.filter(UserModel.email == user_email).first()


def get_user_by_id(user_id: int) -> user_schema.UserOut:

    user = UserModel.filter(UserModel.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found',
        )

    return user_schema.UserOut(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        birth_date=user.birth_date,
    )


def get_users() -> List[user_schema.UserOut]:
    """Get user by database

    This function return a list whith the users.

    Returns: 

        list: list contains the users in json.
    """

    users = UserModel.select()

    list_users = [
        user_schema.UserOut(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            birth_date=user.birth_date,
        )
        for user in users
    ]

    return list_users


def update_user(user_id: int, user_update: user_schema.UserLogin, user: user_schema.UserOut):
    user_reference = UserModel.filter(
        (UserModel.id == user_id) & (UserModel.id == user.id)
    ).first()

    if not user_reference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found',
        )

    # Verify email
    if user_update.email != user_reference.email:
        user_email_reference = get_user(user_update.email)
        if user_email_reference:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Email already registered'
            )

    # Update
    user_reference.first_name = user_update.first_name
    user_reference.last_name = user_update.last_name
    user_reference.email = user_update.email
    user_reference.birth_date = user_update.birth_date

    # Hash password
    user_reference.password = passwords.hash_password(user_update.password)

    user_reference.save()

    return user_schema.UserOut(
        id=user_reference.id,
        first_name=user_reference.first_name,
        last_name=user_reference.last_name,
        email=user_reference.email,
        birth_date=user_reference.birth_date,
    )
