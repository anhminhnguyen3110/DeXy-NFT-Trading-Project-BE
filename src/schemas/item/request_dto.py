import json
from typing import Optional
from pydantic import BaseModel, Field, model_validator, validator
from fastapi import HTTPException, status
from datetime import datetime


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
