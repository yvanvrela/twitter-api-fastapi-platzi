from typing import List

# FastApi
from fastapi import APIRouter, Depends, Body, status, Path, Response

from database.schemas import tweet_schema
from database.schemas.user_schema import UserOut
from ..services import tweet_service
from ..services.auth_service import get_current_user
from utils.db import get_db

router = APIRouter(
    prefix='/api/v1/tweets',
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
    tweet: tweet_schema.TweetBase,
    current_user: UserOut = Depends(get_current_user),
):
    """Create a new tweet

    This path operation create a new tweet in the app and save to database.

    Args:

        tweet (tweet_schema.TweetOut): Tweet base.
        current_user (Token): This is the Token user.

    Returns:

        json: json is the tweet created.
    """
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
    """Get all tweets

    This path operation show all tweets in the app.

    Args:

        current_user (Token): This is the Token user.

    Returns:

        list: the list contains the tweets in json. 
    """
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
    """Get a tweet

    This path operation show a tweet by id in the app.

    Args:

        id (int): This is the tweet id.
        current_user (Token): This is the Token user.

    Returns:

        json: json tweet information.
    """
    return tweet_service.get_tweet(id, current_user)


@router.put(
    path='/{id}',
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary='Update a tweet',
)
async def update_tweet(
    id: int = Path(
        ...,
        gt=0,
        example=1
    ),
    tweet: tweet_schema.TweetBase = Body(...),
    current_user: UserOut = Depends(get_current_user),
):
    """Update a tweet

    This path operation updated a tweet by id in the app.

    Args:

        id (int): This is the tweet id.
        tweet (tweet_schema.TweetBase): This is the Tweet base json.
        current_user (Token): This is the Token user.

    Returns:

        json: json tweet information updated.
    """
    return tweet_service.update_tweet(id, tweet, current_user)


@router.delete(
    path='/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_db)],
    summary='Delete a tweet',
)
async def delete_tweet(
    id: int = Path(
        ...,
        gt=0,
        example=1,
    ),
    current_user: UserOut = Depends(get_current_user),
):
    """Delete a tweet

    This path operation deleted a tweet in the app by id.

    Args:

        id (int): This is the tweet id.
        current_user (Token): This is the Token user.

    Returns:

        status_code: 204
    """

    tweet_service.delte_tweet(id, current_user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
