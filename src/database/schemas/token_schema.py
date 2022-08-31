from pydantic import BaseModel


class Token(BaseModel):
    """Token

    The token model content a token string and type of the token.

    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token Data

    The token data model content information by the token.

    """
    username: str | None = None
