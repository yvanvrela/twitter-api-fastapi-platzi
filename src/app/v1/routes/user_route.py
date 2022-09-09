from typing import List

# FastApi
from fastapi import APIRouter, Depends, Body, status

from database.schemas import user_schema
from ..services import user_service
from utils.db import get_db


router = APIRouter(
    prefix='/api/v1/users',
    tags=['Users'],
)


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_model=List[user_schema.UserOut],
    dependencies=[Depends(get_db)],
    summary='Get all users',
)
async def get_users():
    return user_service.get_users()
