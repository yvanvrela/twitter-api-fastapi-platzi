from pydantic import BaseModel, Field, EmailStr
from datetime import date

# Mixins
from mixins.models_mixin import IDMixin


class UserBase(BaseModel):
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

    email: EmailStr = Field(...)

    birth_date: date | None = Field(
        ...,
        example='1999-01-01',
    )


class UserOut(IDMixin, UserBase):
    pass


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example='secretpassword',
    )
