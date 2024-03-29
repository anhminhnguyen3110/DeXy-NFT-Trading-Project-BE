from typing import Annotated
from fastapi import APIRouter, Body, Depends, File, UploadFile
from fastapi.params import Path
from schemas.item.request_dto import CreateItemRequestDto, GetItemsRequestDto
from schemas.item.response_dto import (
    CreateItemResponseDto,
    GetAnItemResponseDto,
    GetItemsResponseDto,
)
from services.item_service import ItemService
from starlette import status
from utils.auth import get_current_user
from sqlalchemy.orm import Session
from utils.database import get_db

router = APIRouter(
    prefix="/items",
    tags=["Item"],
)
item_service = ItemService()


@router.post(
    "/create-item",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateItemResponseDto,
)
async def create_new_item(
    payload: CreateItemRequestDto = Body(...),
    item_file: UploadFile = File(None),
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return item_service.create_item(payload, item_file, user, db)


@router.get(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetAnItemResponseDto,
)
async def get_an_item(
    item_id: str = Path(
        ...,
        title="item_id",
        example="1",
    ),
    db: Session = Depends(get_db),
):
    return item_service.get_an_item(item_id=item_id, db=db)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=GetItemsResponseDto,
)
async def get_items(
    payload: Annotated[dict, Depends(GetItemsRequestDto)],
    db: Session = Depends(get_db),
):
    return item_service.get_items(payload, db)
