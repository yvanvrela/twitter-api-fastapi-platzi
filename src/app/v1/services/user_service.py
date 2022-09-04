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
        email= user.email,
        birth_date=user.birth_date,
    )


def get_user(user_email: str) -> UserModel:
    """Get user by database

    Filter a user email in database

    Args:

        user_email (str): This is the user email.

    Returns: 

        UserModel: UserModel is a object user.
    """
    return UserModel.filter(UserModel.email == user_email).first()
