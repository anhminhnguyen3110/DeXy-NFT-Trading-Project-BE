from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class CreateItemResponseDto(BaseModel):
    status: str = Field(
        ...,
        example="success",
        description="Status of the response",
        type="string",
    )
    message: str = Field(
        ...,
        example="Item created successfully.",
        description="Description of the response message",
        type="string",
    )
    id: int = Field(
        None, example=10, description="ID of the created item", type="integer"
    )


class GetAnItemDataResponseDto(BaseModel):
    item_id: int = Field(
        ...,
        example=10,
        description="ID of the created item",
        type="integer",
    )
    item_name: str = Field(
        ...,
        example="Dog space",
        description="Name of the created item",
        type="string",
    )
    item_owner_address: str = Field(
        ...,
        example="0x1aBA989D0703cE6CC651B6109d02b39a9651aE5d",
        description="Address of the item owner",
        type="string",
    )
    item_fixed_price: float = Field(
        ...,
        example=0.009,
        description="Fixed price of the item",
        type="number",
    )
    item_currency_type: str = Field(
        ...,
        example="eth",
        description="Currency type of the item",
        type="string",
    )
    item_description: Optional[str] = Field(
        None,
        example="Lorem ipsum dolor sit amet...",
        description="Description of the item",
        type="string",
    )
    item_category_name: str = Field(
        ...,
        example="Animals",
        description="Category of the item",
        type="string",
    )
    item_created_date: datetime = Field(
        ...,
        description="Date when the item was created",
        type="date-time",
    )
    item_created_by_address: str = Field(
        ...,
        example="0x2aFE454D0703cE6CC651B6109d02b39a9651aE5d",
        description="Address of the user who created the item",
        type="string",
    )

    item_image: Optional[str] = Field(
        ...,
        example="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABp",
        description="Base64 encoded image",
        type="string",
    )


class GetAnItemResponseDto(BaseModel):
    data: GetAnItemDataResponseDto
