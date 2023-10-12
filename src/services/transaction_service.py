from repositories.transaction_repository import TransactionRepository
from schemas.pagination.request_dto import BasePaginationRequestDto
from schemas.transaction.response_dto import (
    GetTransactionsDto,
    GetTransactionsSubDto,
)
from utils.database import get_session


class TransactionService:
    def __init__(self):
        self.db = get_session()
        self.transaction_repo = TransactionRepository(self.db)

    def get_transactions(
        self, user_id: int, pagination: BasePaginationRequestDto
    ) -> GetTransactionsDto:
        [
            transactions,
            transaction_count,
        ] = self.transaction_repo.get_transactions(user_id, pagination)

        transaction_list = [
            GetTransactionsSubDto(
                transaction_smart_contract_id=transaction.transaction_smart_contract_id,
                transaction_user_id=transaction.transaction_user_id,
            )
            for transaction in transactions
        ]

        return GetTransactionsDto(
            data=transaction_list,
            total_items=transaction_count,
            items_per_page=pagination.limit,
        )
