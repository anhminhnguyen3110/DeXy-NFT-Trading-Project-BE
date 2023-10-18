from fastapi import HTTPException
from repositories.category_repository import CategoryRepository
from schemas.category.request_dto import CreateCategoryRequestDto
from schemas.category.response_dto import (
    CategoryDataResponseDto,
    CreateCategoryResponseDto,
    GetCategoryResponseDto,
)
from constants.api_error import ErrorMessages

from starlette import status


class CategoryService:
    def __init__(self) -> None:
        self.category_repo = CategoryRepository()
        pass

    def get_categories(self, db) -> GetCategoryResponseDto:
        try:
            categories = self.category_repo.get_categories(db)
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

        return GetCategoryResponseDto(data=res_categories)

    def create_new_category(
        self, payload: CreateCategoryRequestDto, db
    ) -> CreateCategoryResponseDto:
        try:
            self.category_repo.create_category(
                category_name=payload.name,
                category_description=payload.description,
                db=db,
            )
            return CreateCategoryResponseDto(
                status="Success",
                message="Create category successful!",
            )
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.CATEGORY_CREATE_FAILED,
            )
