from models import BaseModel, Field, EmailStr
from uuid import UUID
from datetime import date


class UserBase(BaseModel):
    user_id: UUID | Field(
        ...,
    )
    email = EmailStr = Field(...)


class User(UserBase):
    first_name = str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Juan',
    )
    last_name = str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Vargas',
    )
    birth_date: date | None = Field(
        ...,
        example='1999-01-01',
    )


class UserLogin(UserBase):
    password: str | Field(..., min_length=8, max_length=64,
                          example='secretsecret',)
