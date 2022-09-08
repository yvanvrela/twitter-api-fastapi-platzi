from typing import List, Dict

# FastApi
from datetime import datetime
from fastapi import HTTPException, status

# Models
from database.models.tweet_model import Tweet as TweetModel
from database.schemas import tweet_schema
from database.schemas import user_schema


def create_tweet(tweet: tweet_schema.TweetBase, user: user_schema.UserOut):

    db_tweet = TweetModel(
        content=tweet.content,
        created_at=datetime.now(),
        update_at=datetime.now(),
        by_user=user.id
    )

    db_tweet.save()

    return tweet_schema.TweetOut(
        id=db_tweet.id,
        content=db_tweet.content,
        created_at=db_tweet.created_at,
        update_at=db_tweet.update_at,
        user_id=user.id
    )


def get_tweets(user: user_schema.UserOut) -> List[tweet_schema.TweetOut]:
    # Get tweets by user id
    tweets_by_user = TweetModel.filter(
        TweetModel.by_user == user.id).order_by(TweetModel.update_at.desc())

    list_tweets = [
        tweet_schema.TweetOut(
            id=tweet.id,
            content=tweet.content,
            created_at=tweet.created_at,
            update_at=tweet.update_at,
            user_id=user.id
        )
        for tweet in tweets_by_user
    ]

    return list_tweets


def get_tweet(tweet_id: int, user: user_schema.UserOut) -> dict:
    tweet = TweetModel.filter((TweetModel.id == tweet_id) & (
        TweetModel.by_user == user.id)).first()

    if not tweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tweet not found',
        )

    return tweet_schema.TweetOut(
        id=tweet.id,
        content=tweet.content,
        created_at=tweet.created_at,
        update_at=tweet.update_at,
        user_id=user.id
    )
