from fastapi import APIRouter

users = APIRouter(
    prefix='/users',
    tags=['users'],
)
