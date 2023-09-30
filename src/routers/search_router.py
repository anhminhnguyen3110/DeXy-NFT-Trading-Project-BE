from typing import Annotated
from fastapi import APIRouter, Depends
from starlette import status
from services.search_service import SearchService
from schemas.search.request_dto import SearchRequestDto
from schemas.search.response_dto import SearchResponseDto

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)
search_service = SearchService()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=SearchResponseDto,
)
async def search_users_and_items(
    payload: Annotated[dict, Depends(SearchRequestDto)]
):
    return search_service.search_users_and_items(payload)
