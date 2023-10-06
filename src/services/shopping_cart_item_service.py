from typing import List
from constants.api_error import ErrorMessages
from constants.message import StatusMessages, SuccessMessages
from repositories.item_repository import ItemRepository
from repositories.shopping_cart_item_repository import (
    ShoppingCartItemRepository,
)
from schemas.shopping_cart_item.request_dto import (
    CreateShoppingCartItemRequestDto,
)
from schemas.shopping_cart_item.response_dto import (
    CreateShoppingCartItemsResponseDto,
    DeleteShoppingCartItemsResponseDto,
    GetShoppingCartItemsResponseDto,
    ShoppingCartItemResponseDto,
)
from utils.database import get_session
from starlette import status
from fastapi import HTTPException

from utils.parse_image import parse_image_to_base64


class ShoppingCartItemService:
    def __init__(self):
        self.db = get_session()
        self.shopping_cart_item_repo = ShoppingCartItemRepository(self.db)
        self.item_repo = ItemRepository(self.db)

    def add_item_to_cart(
        self, payload: CreateShoppingCartItemRequestDto, user: dict
    ) -> CreateShoppingCartItemsResponseDto:
        item_id = payload.item_id
        item = self.item_repo.get_item_by_id(item_id)

        if item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=ErrorMessages.ITEM_IS_NOT_EXISTING,
            )

        if item.user.user_id == user["user_id"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.CANNOT_ADD_OWN_ITEM_TO_CART,
            )

        shopping_cart_item = self.shopping_cart_item_repo.get_shopping_cart_item_by_user_id_and_item_id(
            user["user_id"],
            item_id,
        )

        if shopping_cart_item is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.ITEM_ALREADY_IN_CART,
            )

        try:
            self.shopping_cart_item_repo.add_shopping_cart_item(payload, user)
        except Exception as e:
            print(f"Error occurred while adding item to cart: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.SHOPPING_CART_ITEM_CREATION_FAILED,
            )

        return CreateShoppingCartItemsResponseDto(
            message=SuccessMessages.SHOPPING_CART_ITEM_CREATION_SUCCESSFUL,
            status=StatusMessages.SUCCESS,
        )

    def delete_item_from_cart(
        self, item_id: int, user: dict
    ) -> DeleteShoppingCartItemsResponseDto:
        shopping_cart_item = self.shopping_cart_item_repo.get_shopping_cart_item_by_user_id_and_item_id(
            user["user_id"],
            item_id,
        )

        if shopping_cart_item is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.ITEM_NOT_IN_CART,
            )

        try:
            self.shopping_cart_item_repo.delete_shopping_cart_item(
                shopping_cart_item.shopping_cart_item_id
            )

        except Exception as e:
            print(f"Error occurred while deleting item from cart: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.SHOPPING_CART_ITEM_DELETION_FAILED,
            )

        return DeleteShoppingCartItemsResponseDto(
            message=SuccessMessages.SHOPPING_CART_ITEM_DELETION_SUCCESSFUL,
            status=StatusMessages.SUCCESS,
        )

    def get_shopping_cart_items_by_user_wallet(
        self, user: dict
    ) -> GetShoppingCartItemsResponseDto:
        shopping_cart_list = (
            self.shopping_cart_item_repo.get_items_in_cart_by_user_wallet(
                user["wallet_address"]
            )
        )

        item_list: List[ShoppingCartItemResponseDto] = []

        for item in shopping_cart_list:
            item_list.append(
                ShoppingCartItemResponseDto(
                    item_id=item.shopping_cart_item_id,  # Corrected item_id reference
                    item_name=item.item_name,
                    item_fixed_price=item.item_price,
                    item_currency_type=item.item_price_currency,
                    item_image=parse_image_to_base64(item.item_image),
                    item_owner_address=item.user_wallet_address,
                )
            )

        return GetShoppingCartItemsResponseDto(data=item_list)
