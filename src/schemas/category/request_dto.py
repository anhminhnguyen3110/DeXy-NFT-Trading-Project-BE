from pydantic import BaseModel, Field


class CreateCategoryRequestDto(BaseModel):
    name: str = Field(
        ...,
        title="Category name",
        description="Name of the category",
        example="Food",
    )

    description: str = Field(
        None,
        title="Category description",
        description="Description of the category",
        example="Food category",
    )
