from pydantic import BaseModel, Field, EmailStr
from datetime import date


class UserBase(BaseModel):
    user_id: int | Field(
        ...,
        example=1,
    )
    email: EmailStr = Field(...)


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Juan',
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Vargas',
    )
    birth_date: date | None = Field(
        ...,
        example='1999-01-01',
    )


class UserLogin(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example='secretpassword',
    )
