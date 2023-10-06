from fastapi import APIRouter, Depends
from schemas.shopping_cart_item.request_dto import (
    CreateShoppingCartItemRequestDto,
)
from schemas.shopping_cart_item.response_dto import (
    CreateShoppingCartItemsResponseDto,
    DeleteShoppingCartItemsResponseDto,
    GetShoppingCartItemsResponseDto,
)
from services.shopping_cart_item_service import ShoppingCartItemService
from utils.auth import get_current_user
from starlette import status

shopping_cart_items_service = ShoppingCartItemService()

router = APIRouter(
    prefix="/shopping-cart-items",
    tags=["Shopping Cart Items"],
)


@router.post(
    "/add-item",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateShoppingCartItemsResponseDto,
)
def add_item_to_cart(
    payload: CreateShoppingCartItemRequestDto,
    user: dict = Depends(get_current_user),
):
    return shopping_cart_items_service.add_item_to_cart(payload, user)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=GetShoppingCartItemsResponseDto,
)
def get_shopping_cart_items_by_user_wallet(
    user: dict = Depends(get_current_user),
):
    return shopping_cart_items_service.get_shopping_cart_items_by_user_wallet(
        user
    )


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    response_model=DeleteShoppingCartItemsResponseDto,
)
def delete_item_from_cart(item_id: int, user: dict = Depends(get_current_user)):
    return shopping_cart_items_service.delete_item_from_cart(item_id, user)
