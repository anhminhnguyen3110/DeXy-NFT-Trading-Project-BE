from typing import Optional
from pydantic import BaseModel, Field, validator
from starlette import status
from constants.pagination import SortBy
from constants.api_error import ValidationMessages


class PaginationRequestDto(BaseModel):
    page: Optional[int] = Field(
        1,
        description="Page number for pagination (default is 1)",
        example=1,
        type="number",
    )

    limit: Optional[int] = Field(
        10,
        description="Number of items to return per page (default is 10)",
        example=10,
        type="number",
    )

    sort_by: Optional[SortBy] = Field(
        SortBy.PRICE_LOW_TO_HIGH,
        description="Sort by",
        example=SortBy.PRICE_LOW_TO_HIGH,
        type="string",
    )

    @validator("page")
    def page_must_be_positive(cls, v):
        if v is not None and v < 1:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                message=ValidationMessages.PAGE_MUST_BE_POSITIVE,
            )
        if v is not None and v > 100:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                message=ValidationMessages.PAGE_MUST_BE_LESS_THAN_100,
            )
        return v

    @validator("limit")
    def limit_validator(cls, v):
        if v is not None and v < 1:
            raise HttpException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                message=ValidationMessages.LIMIT_MUST_BE_POSITIVE,
            )
        if v is not None and v > 100:
            raise HttpException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                message=ValidationMessages.LIMIT_MUST_BE_LESS_THAN_100,
            )
        return v
