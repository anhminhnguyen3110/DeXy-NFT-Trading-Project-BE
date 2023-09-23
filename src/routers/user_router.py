from fastapi import APIRouter, Body, File, UploadFile
from fastapi.params import Path
from schemas.user.request_dto import CreateUserRequestDto
from schemas.user.response_dto import (
    CreateUserResponseDto,
    GetAnUserResponseDto,
    UpdateUserResponseDto,
)
from services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.post("/users", status_code=201, response_model=CreateUserResponseDto)
async def create_user(payload: CreateUserRequestDto = Body(...)):
    return user_service.create_user(payload=payload)


@router.get(
    "/users/{wallet_address}",
    status_code=200,
    response_model=GetAnUserResponseDto,
)
async def get_an_user(
    wallet_address: str = Path(
        ...,
        title="wallet_address",
        example="0x1aBA989D0703cE6CC651B6109d02b39a9651aE5d",
    )
):
    return user_service.get_an_user(wallet_address=wallet_address)


@router.patch(
    "/users/{wallet_address}",
    status_code=200,
    response_model=UpdateUserResponseDto,
)
async def update_an_user(
    user_image: UploadFile = File(None),
    user_name: str | None = Body(None),
    user_email: str | None = Body(None),
    wallet_address: str = Path(
        ...,
        title="wallet_address",
        example="0x1aBA989D0703cE6CC651B6109d02b39a9651aE5d",
    ),
):
    return user_service.update_an_user(
        wallet_address=wallet_address,
        user_name=user_name,
        user_email=user_email,
        user_image=user_image,
    )
