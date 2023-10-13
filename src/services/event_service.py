from models.transaction_model import TransactionModel
from repositories.item_repository import ItemRepository
from repositories.transaction_repository import TransactionRepository
from repositories.user_repository import UserRepository
from schemas.event.event_dto import TransactionItem
from utils.database import get_session


class EventService:
    def __init__(self) -> None:
        self.db = get_session()
        self.item_repo = ItemRepository(self.db)
        self.user_repo = UserRepository(self.db)
        self.transaction_repo = TransactionRepository(self.db)

    async def handler(self, event: TransactionItem):
        transaction_smart_contract_id = event.transactionId
        owner = event.owner
        buyer = event.buyer
        item_id = event.item

        item = self.item_repo.get_item_by_id(item_id)
        owner = self.user_repo.get_user_by_wallet_address(owner)
        buyer = self.user_repo.get_user_by_wallet_address(buyer)

        if owner is None or buyer is None:
            return

        if (
            item is None
            or item.user.user_wallet_address != owner.user_wallet_address
        ):
            return

        try:
            self.transaction_repo.add_transaction(
                transaction_smart_contract_id, owner.user_id
            )
            self.transaction_repo.add_transaction(
                transaction_smart_contract_id, buyer.user_id
            )

            item.item_owner_id = buyer.user_id

            self.db.commit()
            print("Transaction added successfully")
        except Exception as e:
            print(f"Error: {e}")
            self.db.rollback()  # Rollback if an exception occurs
        finally:
            self.db.close()
