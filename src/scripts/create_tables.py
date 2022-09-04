# Models
from database.models.tweet_model import Tweet
from database.models.user_model import User
# Database
from utils.db import db


def create_tables() -> None:
    with db:
        db.create_tables([User, Tweet])
