from fastapi import APIRouter

tweets = APIRouter(
    prefix='/tweets',
    tags=['Tweet'],
)
