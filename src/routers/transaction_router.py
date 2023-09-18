from abc import ABC
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session

from utils.database import get_session

# from schemas.transaction.request_dto import TransactionCreate  # Import your TransactionCreate schema
from services.transaction_service import (
    TransactionService,
)  # Import your TransactionService

router = APIRouter()


@cbv(router)
class TransactionRouter:
    session: Session = Depends(get_session)

    @router.get("/transactions")
    def get_all(self):
        return TransactionService.get_all(self.session)
