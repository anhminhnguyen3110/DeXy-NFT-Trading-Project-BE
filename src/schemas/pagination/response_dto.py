from typing import Optional
from pydantic import BaseModel, Field


class BasePaginationResponseDto(BaseModel):
    total_items: int = Field(
        ...,
        description="Total number of items across all pages",
        example=100,
        type="number",
    )

    items_per_page: int = Field(
        ...,
        description="Number of items per page",
        example=10,
        type="number",
    )

    total_pages: Optional[int] = Field(
        None,
        description="Total number of pages",
        example=10,
        type="number",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.total_items is not None and self.items_per_page is not None:
            self.total_pages = (
                self.total_items + self.items_per_page - 1
            ) // self.items_per_page
        else:
            self.total_pages = None
