from utils.db import db
from datetime import date
import peewee


class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    birth_date = peewee.DateField(default=date)
    password = peewee.CharField()

    class Meta:
        table_name = 'users'
        database = db
