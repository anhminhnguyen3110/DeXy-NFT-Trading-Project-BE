from fastapi import HTTPException
from web3 import Web3
from repositories.transaction_repository import TransactionRepository
from schemas.pagination.request_dto import BasePaginationRequestDto
from schemas.transaction.response_dto import (
    GetTransactionsDto,
    GetTransactionsSubDto,
)

from utils.web3 import Web3Service
from starlette import status


class TransactionService:
    def __init__(self):
        self.transaction_repo = TransactionRepository()

    def get_transactions(
        self, user_wallet_address: str, pagination: BasePaginationRequestDto, db
    ) -> GetTransactionsDto:
        if not Web3Service.is_address(user_wallet_address):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed! Wallet address {user_wallet_address} is not a valid Ethereum address.",
            )
        user_wallet_address = Web3Service.to_checksum_address(
            user_wallet_address
        )

        [
            transactions,
            transaction_count,
        ] = self.transaction_repo.get_transactions(
            user_wallet_address, pagination, db
        )

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
