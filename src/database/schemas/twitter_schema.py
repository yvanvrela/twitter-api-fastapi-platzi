from pydantic import BaseModel, Field
from mixins.models_mixin import IDMixin
from models.user_model import User
from datetime import datetime


class Tweet(IDMixin,BaseModel):
    
    content: str = Field(
        ...,
        min_length=1,
        max_length=280,
        title='Tweet',
        example='My first tweet',
    )
    created_at: datetime = Field(
        default=datetime.now(),
        title='Creation date',
        example='2020-01-01T00:00:00Z'
    )
    update_at: datetime | None = Field(
        default=None,
        title='Update time',
        example='2020-01-01T00:00:00Z',
    )
    by: User = Field(..., title='User created tweet',)
