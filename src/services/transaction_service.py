from sqlalchemy.orm import Session
from models.transaction_model import (
    Transaction,
)  # Import your Transaction model
from repositories.transaction_repository import (
    TransactionRepository,
)  # Import your TransactionRepository
from utils.database import get_session


class TransactionService:
    def __init__(self):
        self.db = get_session()
        self.transaction_repo = TransactionRepository(self.db)

    def get_all(self) -> list[Transaction]:
        return self.transaction_repo.get_all()

    def create(self, transaction_data) -> Transaction:
        return self.transaction_repo.create_transaction(
            transaction_event=transaction_data.transaction_event,
            transaction_item_name=transaction_data.transaction_item_name,
            transaction_price=transaction_data.transaction_price,
            transaction_from_user_id=transaction_data.transaction_from_user_id,
            transaction_to_user_id=transaction_data.transaction_to_user_id,
            transaction_date=transaction_data.transaction_date,
        )
