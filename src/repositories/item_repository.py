from sqlalchemy.orm import Session
from models.item_model import ItemModel
from schemas.item.request_dto import CreateItemRequestDto


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, item_id):
        return self.db.query(Item).filter(Item.item_id == item_id).first()

    def create_item(self, payload: CreateItemRequestDto):
        new_item = Item(
            item_name=payload.item_name,
            item_owner_id=payload.item_owner_id,
            item_category_id=payload.item_category_id,
            item_price=payload.item_price,
            item_price_currency=payload.item_price_currency,
            item_created_by_address=payload.item_created_by_address,
            item_description=payload.item_description,
            item_image=payload.item_image,
        )
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item

    def update_item(
        self,
        item_id,
        item_name,
        item_owner_id,
        item_category_id,
        item_price,
        item_price_currency,
        item_created_by_address,
        item_description=None,
        item_image=None,
    ):
        item = self.get_by_id(item_id)
        if item:
            item.item_name = item_name
            item.item_owner_id = item_owner_id
            item.item_category_id = item_category_id
            item.item_price = item_price
            item.item_price_currency = item_price_currency
            item.item_created_by_address = item_created_by_address
            item.item_description = item_description
            item.item_image = item_image
            self.db.commit()
            self.db.refresh(item)
            return item
        return None

    def delete_item(self, item_id):
        item = self.get_by_id(item_id)
        if item:
            self.db.delete(item)
            self.db.commit()
            return True
        return False
