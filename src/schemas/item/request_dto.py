from pydantic import BaseModel, Field, validator
from fastapi import HTTPException
from starlette import status


class CreateItemRequestDto(BaseModel):
    name: str = Field(
        ...,
        example="Dog space",
        description="Name of the item",
        type="string",
    )
    description: str = Field(
        ...,
        example="A space for dogs",
        description="Description of the item",
        type="string",
    )
    start_price: str = Field(
        ...,
        example="10.00",
        description="Start price of the item",
        type="string",
    )
    fix_price: str = Field(
        ...,
        example="20.00",
        description="Fixed price of the item",
        type="string",
    )
    create_date: str = Field(
        ...,
        example="8/12/2023 15:44",
        description="Creation date of the item",
        type="string",
    )
    currency_type: str = Field(
        ...,
        example="eth",
        description="Currency type of the item",
        type="string",
    )

    @validator("start_price", "fix_price")
    def validate_price(cls, value: str) -> str:
        try:
            float_value = float(value)
            if float_value < 0:
                raise ValueError("Price must be non-negative")
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Failed! Invalid price format: {value}",
            )
        return value
