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
