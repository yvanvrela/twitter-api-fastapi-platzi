from fastapi import APIRouter

tweets = APIRouter(
    prefix='/users',
    tags=['users'],
)
