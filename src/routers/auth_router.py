from fastapi import APIRouter, Body, Depends
from schemas.auth.request_dto import ConnectWalletRequestDto
from schemas.auth.response_dto import ConnectWalletResponseDto
from starlette import status
from sqlalchemy.orm import Session
from services.auth_service import AuthService
from utils.database import get_db

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
async def connect_wallet(
    payload: ConnectWalletRequestDto = Body(...), db: Session = Depends(get_db)
):
    return auth.connect_wallet(payload=payload, db=db)
