from fastapi import APIRouter

router = APIRouter(
    prefix='/tweets',
    tags=['Tweet'],
)
