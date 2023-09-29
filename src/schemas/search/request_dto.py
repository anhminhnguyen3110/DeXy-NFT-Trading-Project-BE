from pydantic import Field
from schemas.pagination.request_dto import PaginationRequestDto


class SearchRequestDto(PaginationRequestDto):
    search_input: str = Field(
        ...,
        description="Search input",
        example="Dog",
    )
