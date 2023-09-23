from fastapi import HTTPException
from constants.api_error import ErrorMessages
from repositories.item_repository import ItemRepository
from schemas.item.response_dto import CreateItemResponseDto
from schemas.user.request_dto import CreateUserRequestDto
from utils.database import get_session


class ItemService:
    def __init__(self):
        self.db = get_session()
        self.item_repo = ItemRepository(
            self.db
        )  # Use the appropriate ItemRepository

    def create_item(
        self, payload: CreateUserRequestDto
    ) -> CreateItemResponseDto:
        self.item_repo.create_item(payload)
        return CreateItemResponseDto(detail="Success! Created a new item")

    # def get_an_item(self, item_id: int) -> GetAnItemResponseDto:
    #     # Retrieve the item by item_id using the repository
    #     existing_item = self.item_repo.get_item_by_id(item_id)
    #     if not existing_item:
    #         raise HTTPException(
    #             status_code=404, detail=ErrorMessages.ITEM_NOT_FOUND
    #         )
    #     data = {
    #         "item_id": existing_item.item_id,
    #         "item_name": existing_item.item_name,
    #         "item_description": existing_item.item_description,
    #         "item_image": existing_item.item_image,
    #     }

    #     return GetAnItemResponseDto(data=data)
