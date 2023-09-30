from typing import List, Optional
from pydantic import BaseModel, Field
from schemas.pagination.response_dto import BasePaginationResponseDto


class ItemSearchDto(BaseModel):
    item_id: int = Field(
        ...,
        description="The unique identifier for the item",
        example=1,
        type="integer",
    )
    item_name: str = Field(
        ...,
        description="The name of the item",
        example="Dog space",
        type="string",
    )
    item_owner_address: str = Field(
        ...,
        description="The wallet address of the item owner",
        example="0x1aBA989D0703cE6CC651B6109d02b39a9651aE5d",
        type="string",
    )
    item_image: str = Field(
        ...,
        description="The image associated with the item",
        example="base64 encoded string",
        type="string",
    )


class UserSearchDto(BaseModel):
    user_id: int = Field(
        ...,
        description="The unique identifier for the user",
        example=1,
        type="integer",
    )
    user_name: Optional[str] = Field(
        None,
        description="The name of the user",
        example="Dog",
        type="string",
    )
    user_wallet_address: str = Field(
        ...,
        description="The wallet address of the user",
        example="0x1aBA989D0703cE6CC651B6109d02b39a9651aE5d",
        type="string",
    )
    user_image: Optional[str] = Field(
        None,
        description="The image associated with the user",
        example="base64 encoded string",
        type="string",
    )


class ItemsPaginationResponseDto(BasePaginationResponseDto):
    data: List[ItemSearchDto] = Field(
        ...,
        description="List of items",
    )


class UsersPaginationResponseDto(BasePaginationResponseDto):
    data: List[UserSearchDto] = Field(
        ...,
        description="List of users",
    )


class SearchResponseDto(BaseModel):
    items: ItemsPaginationResponseDto
    users: UsersPaginationResponseDto
