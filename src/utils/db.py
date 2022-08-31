from contextvars import ContextVar
from fastapi import Depends
import peewee

# Import settings class
from app.v1.config.settings import Settings

# Instance Settings class
settings = Settings()

# Save settings var in consts
DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port


# DB state configurations
db_state_default = {
    'closed': None,
    'conn': None,
    'ctx': None,
    'transactions': None
}
db_state = ContextVar('db_state', default=db_state_default.copy())


# Set connection status to work local
class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__('_state', db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value) -> None:
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


# Init db connection
db = peewee.PostgresqlDatabase(
    database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

# Overwrite the '_state' internal attribute, using the new Peewe Config
db._state = PeeweeConnectionState()


# Functions to use the database
async def reset_db_state() -> None:
    """Reset Database State

    Set a database state default and reset the database

    """
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)) -> None:
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()
