import json
from typing import Optional
from pydantic import BaseModel, Field, model_validator, validator
from fastapi import HTTPException, status
from datetime import datetime

from schemas.pagination.request_dto import BasePaginationRequestDto
from constants.pagination import SortBy
from utils.web3 import Web3Service


class CreateItemRequestDto(BaseModel):
    name: str = Field(
        ...,
        example="Dog space",
        description="Name of the item",
        type="string",
    )
    fix_price: float = Field(
        ...,
        example="20.00",
        description="Fixed price of the item",
        type="number",
    )
    create_date: datetime = Field(
        ...,
        description="Creation date of the item",
        type="date-time",
    )
    category_id: Optional[int] = Field(
        ...,
        example=1,
        description="Category ID of the item",
        type="integer",
    )
    currency_type: Optional[str] = Field(
        "eth",
        example="eth",
        description="Currency type of the item",
        type="string",
    )
    description: Optional[str] = Field(
        None,
        example="A space for dogs",
        description="Description of the item",
        type="string",
    )

    @model_validator(mode="before")
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value

    @validator("fix_price")
    def validate_price(cls, value: str) -> str:
        try:
            float_value = float(value)
            if float_value < 0:
                raise ValueError("Price must be non-negative")
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Invalid price format: {value}",
            )
        return value


class GetItemsRequestDto(BasePaginationRequestDto):
    sort_by: Optional[SortBy] = Field(
        SortBy.PRICE_LOW_TO_HIGH,
        description="Get item by sort by",
        example=SortBy.PRICE_LOW_TO_HIGH,
        type="string",
    )

    search_input: Optional[str] = Field(
        None,
        description="Get item by name",
        example="Dog",
        type="string",
    )

    price_start: Optional[float] = Field(
        None,
        description="Get item by price start",
        example=0.00,
        type="number",
    )

    price_end: Optional[float] = Field(
        None,
        description="Get item by price end",
        example=100.00,
        type="number",
    )

    category_id: Optional[int] = Field(
        None,
        description="Get item by category id",
        example=1,
        type="integer",
    )

    user_wallet_address: Optional[str] = Field(
        None,
        description="Get item by owner wallet address",
        example="0xF8604Bfd06a6fc2Fb2020547a4fF41e64029BC66",
        type="string",
    )

    @validator("user_wallet_address")
    def validate_wallet_address(cls, value: str) -> str:
        if not Web3Service.is_address(value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Failed! Wallet address {value} is not a valid Ethereum address.",
            )
        checksum_address = Web3Service.to_checksum_address(value)
        return checksum_address
