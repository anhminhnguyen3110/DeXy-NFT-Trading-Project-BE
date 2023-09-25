from pydantic import BaseModel, Field
from typing import Optional


class CreateItemResponseDto(BaseModel):
    status: str = Field(..., example="success")
    message: str = Field(..., example="Item created successfully.")
    id: Optional[int] = Field(
        ..., examples=10, description="ID of the created item"
    )
