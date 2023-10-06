from typing import List, Optional
from pydantic import BaseModel, Field

from constants.message import StatusMessages


class CreateShoppingCartItemsResponseDto(BaseModel):
    status: str = Field(
        ...,
        example=StatusMessages.SUCCESS,
        description="Status of the response",
        type="string",
    )
    message: str = Field(
        ...,
        example="Item created successfully.",
        description="Description of the response message",
        type="string",
    )


class DeleteShoppingCartItemsResponseDto(BaseModel):
    status: str = Field(
        ...,
        example=StatusMessages.SUCCESS,
        description="Status of the response",
        type="string",
    )
    message: str = Field(
        ...,
        example="Item deleted successfully.",
        description="Description of the response message",
        type="string",
    )


class ShoppingCartItemResponseDto(BaseModel):
    item_id: int = Field(
        ...,
        example=1,
        description="Item ID of the item to be added to the shopping cart.",
    )

    item_name: str = Field(
        ...,
        example="Item Name",
        description="Name of the item to be added to the shopping cart.",
    )

    item_owner_address: str = Field(
        ...,
        example="0x0",
        description="Address of the item owner.",
    )

    item_fixed_price: float = Field(
        ...,
        example=1.0,
        description="Fixed price of the item.",
    )

    item_currency_type: str = Field(
        ...,
        example="ETH",
        description="Currency type of the item.",
    )

    item_image: Optional[str] = Field(
        None,
        example="binary object",
        description="Image of the item.",
    )


class GetShoppingCartItemsResponseDto(BaseModel):
    data: List[ShoppingCartItemResponseDto]
