from typing import Annotated
from fastapi import APIRouter, Depends, Path
from starlette import status
from schemas.pagination.request_dto import BasePaginationRequestDto
from services.transaction_service import TransactionService
from sqlalchemy.orm import Session
from utils.database import get_db

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)

transactionService = TransactionService()


@router.get(
    "/{user_wallet_address}",
    status_code=status.HTTP_200_OK,
)
async def get_transactions(
    pagination: Annotated[dict, Depends(BasePaginationRequestDto)],
    user_wallet_address: str = Path(
        ...,
        title="user_wallet_address",
        example="0xDA70e2502Ec52C380ACcA7f998fb8271779A3168",
    ),
    db: Session = Depends(get_db),
):
    return transactionService.get_transactions(
        user_wallet_address, pagination, db
    )
