from models.shopping_cart_item_model import ShoppingCartItemModel
from repositories.item_repository import ItemRepository
from repositories.shopping_cart_item_repository import (
    ShoppingCartItemRepository,
)
from repositories.transaction_repository import TransactionRepository
from repositories.user_repository import UserRepository
from schemas.event.event_dto import TransactionItem
from sqlalchemy.orm import Session


class EventService:
    def __init__(self) -> None:
        self.item_repo = ItemRepository()
        self.user_repo = UserRepository()
        self.transaction_repo = TransactionRepository()
        self.shopping_cart_repo = ShoppingCartItemRepository()

    async def handler(self, event: TransactionItem, db: Session):
        transaction_smart_contract_id = event.transactionId
        owner = event.owner
        buyer = event.buyer
        item_id = event.item

        owner = self.user_repo.get_user_by_wallet_address(owner, db)
        buyer = self.user_repo.get_user_by_wallet_address(buyer, db)
        shopping_cart_item = self.shopping_cart_repo.get_shopping_cart_item_by_user_id_and_item_id(
            buyer.user_id, item_id, db
        )
        item = self.item_repo.get_item_by_id_maintain_session(item_id, db)
        if owner is None or buyer is None:
            print("Owner or buyer not found")
            return
        if item is None:
            print("Item not found")
            return
        if item.user.user_wallet_address != owner.user_wallet_address:
            print("Owner is not the owner of the item")
            return

        try:
            self.transaction_repo.add_transaction(
                transaction_smart_contract_id, owner.user_id, db
            )
            self.transaction_repo.add_transaction(
                transaction_smart_contract_id, buyer.user_id, db
            )

            item.item_owner_id = buyer.user_id
            if shopping_cart_item is not None:
                db.query(ShoppingCartItemModel).filter(
                    ShoppingCartItemModel.shopping_cart_item_id
                    == shopping_cart_item.shopping_cart_item_id
                ).delete()
            db.commit()
            print("Transaction added successfully")
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
