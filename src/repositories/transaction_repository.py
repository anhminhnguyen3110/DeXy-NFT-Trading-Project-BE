from models.transaction_model import TransactionModel
from sqlalchemy.orm import Session

from schemas.pagination.request_dto import BasePaginationRequestDto


class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_transaction(
        self, transaction_smart_contract_id: int, transaction_user_id: int
    ):
        transaction = TransactionModel(
            transaction_smart_contract_id=transaction_smart_contract_id,
            transaction_user_id=transaction_user_id,
        )
        self.db.add(transaction)

    def get_transactions(
        self, user_id: int, pagination: BasePaginationRequestDto
    ):
        return [
            self.db.query(
                TransactionModel.transaction_smart_contract_id.label(
                    "transaction_smart_contract_id"
                ),
                TransactionModel.transaction_user_id.label(
                    "transaction_user_id"
                ),
            )
            .filter_by(transaction_user_id=user_id)
            .all(),
            self.db.query(TransactionModel)
            .filter_by(transaction_user_id=user_id)
            .count(),
        ]
