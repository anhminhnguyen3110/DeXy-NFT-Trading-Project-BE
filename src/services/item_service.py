from sqlalchemy.orm import Session
from models.item_model import Item
from repositories.item_repository import ItemRepository


class ItemService:
    def __init__(self):
        self.db = get_session()
        self.item_repo = ItemRepository(self.db)

    def get_all(self) -> list[Item]:
        return self.item_repo.get_all()

    def get_by_id(self, item_id: int) -> Item:
        return self.item_repo.get_by_id(item_id)

    def create(self, item_data) -> Item:
        return self.item_repo.create_item(
            item_name=item_data.item_name,
            item_owner_id=item_data.item_owner_id,
            item_category_id=item_data.item_category_id,
            item_price=item_data.item_price,
            item_price_currency=item_data.item_price_currency,
            item_created_by_address=item_data.item_created_by_address,
            item_description=item_data.item_description,
            item_image=item_data.item_image,
        )

    def update(self, item_id: int, item_data) -> Item:
        return self.item_repo.update_item(
            item_id=item_id,
            item_name=item_data.item_name,
            item_owner_id=item_data.item_owner_id,
            item_category_id=item_data.item_category_id,
            item_price=item_data.item_price,
            item_price_currency=item_data.item_price_currency,
            item_created_by_address=item_data.item_created_by_address,
            item_description=item_data.item_description,
            item_image=item_data.item_image,
        )

    def delete_by_id(self, item_id: int):
        return self.item_repo.delete_item(item_id)
