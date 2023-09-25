from fastapi import APIRouter, Body
from schemas.auth.request_dto import ConnectWalletRequestDto
from schemas.auth.response_dto import ConnectWalletResponseDto
from starlette import status
from services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)
auth = AuthService()


@router.post(
    "",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ConnectWalletResponseDto,
)
async def connect_wallet(payload: ConnectWalletRequestDto = Body(...)):
    return auth.connect_wallet(payload=payload)
