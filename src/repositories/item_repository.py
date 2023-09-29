from sqlalchemy import func
from sqlalchemy.orm import Session
from models.item_model import ItemModel
from schemas.item.request_dto import CreateItemRequestDto
from schemas.search.request_dto import SearchRequestDto


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_item_by_id(self, item_id) -> ItemModel:
        return (
            self.db.query(ItemModel)
            .filter(ItemModel.item_id == item_id)
            .first()
        )

    def create_item(
        self,
        payload: CreateItemRequestDto,
        item_file,
        owner_id: int,
        owner_address: str,
    ) -> int:
        if payload.currency_type is None:
            payload.currency_type = "eth"
        new_item = ItemModel(
            item_name=payload.name,
            item_owner_id=owner_id,
            item_category_id=payload.category_id,
            item_price=payload.fix_price,
            item_price_currency=payload.currency_type,
            item_created_by_address=owner_address,
            item_description=payload.description,
            item_image=item_file,
        )
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item.item_id

    def search_items(self, payload: SearchRequestDto) -> list[ItemModel]:
        page = payload.page
        limit = payload.limit
        search_input = payload.search_input.lower()

        query = self.db.query(ItemModel).filter(
            func.lower(ItemModel.item_name).like(f"{search_input}%")
        )

        items = query.offset((page - 1) * limit).limit(limit).all()

        return items
