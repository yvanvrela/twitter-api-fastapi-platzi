from models.user_model import User
from utils.db import db
from datetime import datetime
import peewee


# One to Many relationship
class Tweet(peewee.Model):
    # The id created automatic by peewee
    content = peewee.TextField()
    created_at = peewee.DateTimeField(default=datetime.now())
    update_at = peewee.DateTimeField(default=None)
    by_user = peewee.ForeignKeyField(model=User, backref='tweets')

    # The database connection
    class Meta:
        table_name = 'tweets'
        database = db
