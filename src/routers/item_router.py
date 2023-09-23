from typing import Annotated
from fastapi import APIRouter, Body, Depends, Security
from schemas.item.request_dto import CreateItemRequestDto
from schemas.item.response_dto import CreateItemResponseDto
from services.item_service import ItemService
from starlette import status
from utils.auth import get_current_user

router = APIRouter(
    prefix="/items",
    tags=["Item"],
)
item_service = ItemService()


# @router.post(
#     "/create",
#     status_code=status.HTTP_201_CREATED,
#     response_model=CreateItemResponseDto,
# )
# async def create_item(
#     payload: Annotated[dict, Depends(CreateItemRequestDto)] = Body(...)
# ):
#     return item_service.create_item(payload=payload)


@router.post(
    "",
    status_code=200,
)
async def get_an_item(payload: str, user: dict = Security(get_current_user)):
    return "Done"
