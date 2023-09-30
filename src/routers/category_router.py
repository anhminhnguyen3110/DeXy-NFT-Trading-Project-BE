from fastapi import APIRouter
from starlette import status

from services.category_service import CategoryService
from schemas.category.response_dto import CategoryResponseDto

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)

category_service = CategoryService()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=CategoryResponseDto,
)
async def get_categories():
    return category_service.get_categories()
