from repositories.category_repository import CategoryRepository
from schemas.category.response_dto import (
    CategoryDataResponseDto,
    CategoryResponseDto,
)
from constants.api_error import ErrorMessages
from utils.database import get_session
from starlette import status


class CategoryService:
    def __init__(self) -> None:
        self.db = get_session()
        self.category_repo = CategoryRepository(self.db)
        pass

    def get_categories(self) -> CategoryResponseDto:
        try:
            categories = self.category_repo.get_categories()
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.CATEGORY_GET_FAILED,
            )
        res_categories = [
            CategoryDataResponseDto(
                category_id=category.category_id,
                category_name=category.category_name,
                category_description=category.category_description,
            )
            for category in categories
        ]

        return CategoryResponseDto(data=res_categories)
