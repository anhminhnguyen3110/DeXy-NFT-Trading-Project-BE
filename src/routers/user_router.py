from typing import Annotated
from fastapi import APIRouter, Body, File, UploadFile, Depends
from fastapi.params import Path
from schemas.user.request_dto import CreateUserRequestDto, UpdateUserRequestDto
from schemas.user.response_dto import (
    CreateUserResponseDto,
    GetAnUserResponseDto,
    UpdateUserResponseDto,
)
from starlette import status
from services.user_service import UserService
from utils.auth import get_current_user
from sqlalchemy.orm import Session
from utils.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["User"],
)
user_service = UserService()


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateUserResponseDto,
)
async def create_user(
    payload: Annotated[dict, Depends(CreateUserRequestDto)],
    db: Session = Depends(get_db),
):
    return user_service.create_user(payload=payload, db=db)


@router.get(
    "/{wallet_address}",
    status_code=status.HTTP_200_OK,
    response_model=GetAnUserResponseDto,
)
async def get_an_user(
    wallet_address: str = Path(
        ...,
        title="wallet_address",
        example="0x1aBA989D0703cE6CC651B6109d02b39a9651aE5d",
    ),
    db: Session = Depends(get_db),
):
    return user_service.get_an_user(wallet_address=wallet_address, db=db)


@router.patch(
    "/edit",
    status_code=status.HTTP_200_OK,
    response_model=UpdateUserResponseDto,
)
async def update_an_user(
    payload: UpdateUserRequestDto = Body(...),
    user_image: UploadFile = File(None),
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return user_service.update_an_user(payload, user_image, user, db)
