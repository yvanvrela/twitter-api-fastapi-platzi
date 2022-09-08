from typing import List

# FastApi
from fastapi import APIRouter, Depends, Body, status, Path

from database.schemas import tweet_schema
from database.schemas.user_schema import UserOut
from ..services import tweet_service
from ..services.auth_service import get_current_user
from utils.db import get_db

router = APIRouter(
    prefix='/tweets',
    tags=['Tweet'],
)


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    response_model=tweet_schema.TweetOut,
    dependencies=[Depends(get_db)],
    summary='Create a new tweet',
)
async def create_tweet(
    tweet: tweet_schema.TweetOut,
    current_user: UserOut = Depends(get_current_user),
):
    return tweet_service.create_tweet(tweet, current_user)


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_model=List[tweet_schema.TweetOut],
    dependencies=[Depends(get_db)],
    summary='Get all tweets',
)
async def get_tweets(
    current_user: UserOut = Depends(get_current_user)
):
    return tweet_service.get_tweets(current_user)


@router.get(
    path='/{id}',
    status_code=status.HTTP_200_OK,
    response_model=tweet_schema.TweetOut,
    dependencies=[Depends(get_db)],
    summary='Get a tweet',
)
async def get_tweets(
    id: int = Path(
        ...,
        gt=0,
        example=1,
    ),
    current_user: UserOut = Depends(get_current_user)
):
    return tweet_service.get_tweet(id, current_user)
