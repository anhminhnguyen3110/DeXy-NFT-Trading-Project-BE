from typing import List, Optional
from pydantic import BaseModel, Field


class CategoryDataResponseDto(BaseModel):
    category_id: int = Field(
        ...,
        title="Category ID",
        example=1,
        description="Category ID",
    )

    category_name: str = Field(
        ...,
        title="Category Name",
        example="Animals",
        description="Category Name",
    )

    category_description: Optional[str] = Field(
        None,
        title="Category Description",
        example="This is the category description",
        description="Category Description",
    )


class CategoryResponseDto(BaseModel):
    data: List[CategoryDataResponseDto]
