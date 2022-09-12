""" All settings of the proyect """

import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Private var
    _db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')

    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

    @property
    def db_name(self):
        """Change the db name

        This function change the database name, if running of test.

        Returns:

            str: str database.
        """
        if os.getenv('RUN_ENV') == 'test':
            return f'test_{self._db_name}'

        return self._db_name
