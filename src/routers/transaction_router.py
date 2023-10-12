from typing import Annotated
from fastapi import APIRouter, Depends, Path
from starlette import status

from schemas.pagination.request_dto import BasePaginationRequestDto
from services.transaction_service import TransactionService


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)

transactionService = TransactionService()


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
)
async def get_transactions(
    pagination: Annotated[dict, Depends(BasePaginationRequestDto)],
    user_id: int = Path(
        ...,
        title="user_id",
        example="1",
    ),
):
    return transactionService.get_transactions(user_id, pagination)
