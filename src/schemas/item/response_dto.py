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
