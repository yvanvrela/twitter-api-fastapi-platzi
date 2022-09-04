from utils.db import db
import peewee


class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    birth_date = peewee.DateField()
    password = peewee.CharField()

    class Meta:
        table_name = 'users'
        database = db
