from fastapi import APIRouter, Depends, Body, status
from database.schemas import user_schema



router = APIRouter(
    prefix='/api/v1/users',
    tags=['User'],
)

