from sqlalchemy.orm import Session
from models.transaction_model import (
    Transaction,
)  # Import your Transaction model here


class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, transaction_id):
        return (
            self.db.query(Transaction)
            .filter(Transaction.transaction_id == transaction_id)
            .first()
        )

    def create_transaction(
        self,
        transaction_event,
        transaction_item_name,
        transaction_price,
        transaction_from_user_id,
        transaction_to_user_id,
        transaction_date,
    ):
        new_transaction = Transaction(
            transaction_event=transaction_event,
            transaction_item_name=transaction_item_name,
            transaction_price=transaction_price,
            transaction_from_user_id=transaction_from_user_id,
            transaction_to_user_id=transaction_to_user_id,
            transaction_date=transaction_date,
        )
        self.db.add(new_transaction)
        self.db.commit()
        self.db.refresh(new_transaction)
        return new_transaction

    def update_transaction(
        self,
        transaction_id,
        transaction_event,
        transaction_item_name,
        transaction_price,
        transaction_from_user_id,
        transaction_to_user_id,
        transaction_date,
    ):
        transaction = self.get_by_id(transaction_id)
        if transaction:
            transaction.transaction_event = transaction_event
            transaction.transaction_item_name = transaction_item_name
            transaction.transaction_price = transaction_price
            transaction.transaction_from_user_id = transaction_from_user_id
            transaction.transaction_to_user_id = transaction_to_user_id
            transaction.transaction_date = transaction_date
            self.db.commit()
            self.db.refresh(transaction)
            return transaction
        return None

    def delete_transaction(self, transaction_id):
        transaction = self.get_by_id(transaction_id)
        if transaction:
            self.db.delete(transaction)
            self.db.commit()
            return True
        return False
