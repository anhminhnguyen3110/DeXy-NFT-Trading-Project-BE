from fastapi import HTTPException
from pydantic import BaseModel, Field, validator
from starlette import status


class CreateShoppingCartItemRequestDto(BaseModel):
    item_id: int = Field(
        ...,
        example=1,
        description="Item ID of the item to be added to the shopping cart.",
    )

    @validator("item_id")
    def item_id_must_be_positive_integer(cls, v):
        if v <= 0:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Item ID must be a positive integer.",
            )
        if not isinstance(v, int):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Item ID must be an integer.",
            )
        return v
