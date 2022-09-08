from datetime import datetime, timedelta

# FastApi
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from database.models.user_model import User as UserModel
from database.schemas.token_schema import TokenData
from utils.passwords import verify_password
from ..config.settings import Settings
from .user_service import get_user

settings = Settings()


# Conts of jwt
SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.token_expire

# Instance the login url and to validate token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login/")


def authenticate_user(user_email: str, password: str) -> UserModel | bool:
    """Authenticate user

    This is function recibed the username and password and verify to exists and the password is correct.

    Args:

        user_email (str): This is the user email.
        password (str): This is the user password.

    Returns:

        UserModel | bool: UserModel is the user object or bool default is False.
    """
    user = get_user(user_email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expieres_delta: timedelta | None = None) -> str:
    """Create access token

    This is function recibed the user information and expire time of save in the token. 

    Args:

        data (dict): This is the user information to encode.
        expieres_delta (timedelta | optional): This the expire time. Defaults to None.

    Returns:

        str: str is the user token.
    """

    to_encode = data.copy()

    if expieres_delta:
        expire = datetime.utcnow() + expieres_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def generate_token(user_email: str, password: str) -> str:
    """Generate token

    This is function generate a token by the user email and password.

    Args:

        user_email (str): This is the user email.
        password (str): This is the user password.

    Raises:

        HTTPException: code: 401, detail: Incorrect email or password.

    Returns:

        str: str is the user token.
    """
    # Validate the data
    user = authenticate_user(user_email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    return create_access_token(
        data={
            'sub': user.email,
        },
        expieres_delta=access_token_expires
    )


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserModel:
    """Get current user

    This is function recibed a token and verify the token is correct.

    Args:

        token (str): This is the user token. Defaults to Depends(oauth2_scheme).

    Raises:

        credentials_exception: code:401, detail:Could not validate credentials, headers:{WWW-Authenticate: Bearer} 

    Returns:
        UserModel: UserModel is the user object
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_email: str = payload.get('sub')
        if user_email is None:
            raise credentials_exception

        token_data = TokenData(user_email=user_email)
    except JWTError:
        raise credentials_exception

    user = get_user(user_email=token_data.user_email)
    if user is None:
        raise credentials_exception
    return user
