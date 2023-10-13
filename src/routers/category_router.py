from typing import Annotated
from fastapi import APIRouter, Depends
from starlette import status
from schemas.category.request_dto import CreateCategoryRequestDto

from services.category_service import CategoryService
from schemas.category.response_dto import (
    CreateCategoryResponseDto,
    GetCategoryResponseDto,
)

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
async def get_categories():
    return category_service.get_categories()


@router.post(
    "",
    status_code=status.HTTP_200_OK,
    response_model=CreateCategoryResponseDto,
)
async def create_category(
    payload: Annotated[dict, Depends(CreateCategoryRequestDto)]
):
    return category_service.create_new_category(payload)
