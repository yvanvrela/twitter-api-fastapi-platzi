from pydantic import BaseModel, Field
from mixins.models_mixin import IDMixin
from database.schemas.user_schema import UserOut
from datetime import datetime


class TweetBase(BaseModel):
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


class TweetOut(IDMixin, TweetBase):
    user_id: int = Field(
        ...,
        ge=1,
        title='User who created the tweet',
        example=1,
    )


class TweetRelations(IDMixin, TweetBase):
    by_user: UserOut = Field(..., title='User created tweet',)
