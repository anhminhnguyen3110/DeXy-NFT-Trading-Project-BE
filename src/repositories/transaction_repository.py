from models.transaction_model import TransactionModel
from sqlalchemy.orm import Session
from models.user_model import UserModel

from schemas.pagination.request_dto import BasePaginationRequestDto


class TransactionRepository:
    def add_transaction(
        self, transaction_smart_contract_id: int, transaction_user_id: int, db
    ):
        transaction = TransactionModel(
            transaction_smart_contract_id=transaction_smart_contract_id,
            transaction_user_id=transaction_user_id,
        )
        db.add(transaction)

    def get_transactions(
        self, user_wallet_address: str, pagination: BasePaginationRequestDto, db
    ):
        query = (
            db.query(
                TransactionModel.transaction_smart_contract_id.label(
                    "transaction_smart_contract_id"
                ),
                TransactionModel.transaction_user_id.label(
                    "transaction_user_id"
                ),
            )
            .join(
                UserModel,
                UserModel.user_id == TransactionModel.transaction_user_id,
            )
            .filter(UserModel.user_wallet_address == user_wallet_address)
        )

        total_count = query.count()

        transactions = (
            query.offset((pagination.page - 1) * pagination.limit)
            .limit(pagination.limit)
            .all()
        )

        return transactions, total_count
