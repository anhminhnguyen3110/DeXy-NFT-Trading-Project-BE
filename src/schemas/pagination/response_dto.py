from pydantic import BaseModel, Field


class PaginationResponseDto(BaseModel):
    total_items: int = Field(
        ...,
        description="Total number of items across all pages",
        example=100,
        type="number",
    )
    item_per_page: int = Field(
        ...,
        description="Current page number",
        example=10,
        type="number",
    )
    total_pages: int = Field(
        ...,
        description="Total number of pages",
        example=10,
        type="number",
    )
