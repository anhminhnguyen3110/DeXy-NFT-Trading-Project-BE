from fastapi import HTTPException, UploadFile
from constants.api_error import ErrorMessages
from repositories.item_repository import ItemRepository
from schemas.item.response_dto import CreateItemResponseDto
from schemas.user.request_dto import CreateUserRequestDto
from repositories.category_repository import CategoryRepository
from utils.database import get_session
from starlette import status


class ItemService:
    def __init__(self):
        self.db = get_session()
        self.item_repo = ItemRepository(self.db)
        self.category_repo = CategoryRepository(self.db)

    def create_item(
        self, payload: CreateUserRequestDto, item_file: UploadFile, user: dict
    ) -> CreateItemResponseDto:
        category = self.category_repo.get_category_by_id(payload.category_id)
        if category == None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.CATEGORY_IS_NOT_EXISTING,
            )

        binary_file = None
        if item_file:
            try:
                binary_file = item_file.file.read()
                item_file.file.close()
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=e,
                )
        try:
            id = self.item_repo.create_item(
                payload=payload, item_file=binary_file, owner_id=user["user_id"]
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.ITEM_CREATION_FAILED,
            )

        return CreateItemResponseDto(
            status="Success",
            message="Item created successfully.",
            id=id,
        )
