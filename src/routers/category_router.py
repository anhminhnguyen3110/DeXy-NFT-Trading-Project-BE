from typing import Annotated
from fastapi import APIRouter, Depends
from starlette import status
from schemas.category.request_dto import CreateCategoryRequestDto
from services.category_service import CategoryService
from schemas.category.response_dto import (
    CreateCategoryResponseDto,
    GetCategoryResponseDto,
)
from sqlalchemy.orm import Session
from utils.database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)

category_service = CategoryService()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=GetCategoryResponseDto,
)
async def get_categories(db: Session = Depends(get_db)):
    return category_service.get_categories(db)


@router.post(
    "",
    status_code=status.HTTP_200_OK,
    response_model=CreateCategoryResponseDto,
)
async def create_category(
    payload: Annotated[dict, Depends(CreateCategoryRequestDto)],
    db: Session = Depends(get_db),
):
    return category_service.create_new_category(payload, db)
