from pydantic import Field
from schemas.pagination.request_dto import BasePaginationRequestDto


class SearchRequestDto(BasePaginationRequestDto):
    search_input: str = Field(
        ...,
        description="Search input",
        example="Dog",
    )
