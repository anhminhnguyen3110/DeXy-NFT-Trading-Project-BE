from fastapi import HTTPException, UploadFile
from constants.api_error import ErrorMessages
from repositories.item_repository import ItemRepository
from schemas.item.response_dto import (
    CreateItemResponseDto,
    GetAnItemDataResponseDto,
    GetAnItemResponseDto,
    GetItemsDataResponseDto,
    GetItemsResponseDto,
)
from schemas.user.request_dto import CreateUserRequestDto
from repositories.category_repository import CategoryRepository
from schemas.item.request_dto import GetItemsRequestDto
from utils.parse_image import parse_image_to_base64

from starlette import status


class ItemService:
    def __init__(self):
        self.item_repo = ItemRepository()
        self.category_repo = CategoryRepository()

    def create_item(
        self,
        payload: CreateUserRequestDto,
        item_file: UploadFile,
        user: dict,
        db,
    ) -> CreateItemResponseDto:
        category = self.category_repo.get_category_by_id(
            payload.category_id, db
        )
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
                payload=payload,
                item_file=binary_file,
                owner_id=user["user_id"],
                owner_address=user["wallet_address"],
                db=db,
            )
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.ITEM_CREATION_FAILED,
            )

        return CreateItemResponseDto(
            status="Success",
            message="Item created successfully.",
            id=id,
        )

    def get_an_item(self, item_id: int, db) -> GetAnItemResponseDto:
        item = self.item_repo.get_item_by_id(item_id, db)
        if item == None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.ITEM_IS_NOT_EXISTING,
            )
        item_image = parse_image_to_base64(item.item_image)
        return GetAnItemResponseDto(
            data=GetAnItemDataResponseDto(
                item_id=item.item_id,
                item_name=item.item_name,
                item_owner_address=item.user.user_wallet_address,
                item_description=item.item_description,
                item_category_name=item.category.category_name,
                item_fixed_price=item.item_price,
                item_currency_type=item.item_price_currency,
                item_created_date=item.item_created_date,
                item_created_by_address=item.item_created_by_address,
                item_image=item_image,
            )
        )

    def get_items(self, payload: GetItemsRequestDto, db) -> GetItemsResponseDto:
        [items, items_count] = self.item_repo.get_items(payload, db)
        res_items = [
            GetItemsDataResponseDto(
                item_id=item.item_id,
                item_name=item.item_name,
                item_owner_address=item.user.user_wallet_address,
                item_category_name=item.category.category_name,
                item_fixed_price=item.item_price,
                item_currency_type=item.item_price_currency,
                item_image=parse_image_to_base64(item.item_image),
            )
            for item in items
        ]

        return GetItemsResponseDto(
            data=res_items,
            total_items=items_count,
            items_per_page=payload.limit,
        )
