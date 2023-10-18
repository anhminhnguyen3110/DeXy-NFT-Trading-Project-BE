from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from models.item_model import ItemModel
from schemas.item.request_dto import CreateItemRequestDto, GetItemsRequestDto
from schemas.search.request_dto import SearchRequestDto
from constants.pagination import SortBy
from models.user_model import UserModel


class ItemRepository:
    def get_item_by_id(self, item_id, db) -> ItemModel:
        query = db.query(ItemModel).filter(ItemModel.item_id == item_id)

        return query.first()

    def create_item(
        self,
        payload: CreateItemRequestDto,
        item_file,
        owner_id: int,
        owner_address: str,
        db,
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
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

        return new_item.item_id

    def search_items(self, payload: SearchRequestDto, db):
        page = payload.page
        limit = payload.limit
        search_input = payload.search_input.lower()

        query = db.query(ItemModel).filter(
            func.lower(ItemModel.item_name).like(f"{search_input}%")
        )
        items_count = query
        items = query.offset((page - 1) * limit).limit(limit)

        return [items.all(), items_count.count()]

    def get_items(self, payload: GetItemsRequestDto, db) -> list[ItemModel]:
        query = db.query(ItemModel)

        # Filter by category_id
        if payload.category_id:
            query = query.filter(
                ItemModel.item_category_id == payload.category_id
            )

        # Filter by user_wallet_address
        if payload.user_wallet_address is not None:
            query = query.join(ItemModel.user).filter(
                UserModel.user_wallet_address == payload.user_wallet_address
            )

        # Filter by price range
        if payload.price_start is not None:
            query = query.filter(ItemModel.item_price >= payload.price_start)
        if payload.price_end is not None:
            query = query.filter(ItemModel.item_price <= payload.price_end)

        # Sorting based on sort_by enum
        if payload.sort_by == SortBy.PRICE_LOW_TO_HIGH:
            query = query.order_by(ItemModel.item_price)
        elif payload.sort_by == SortBy.PRICE_HIGH_TO_LOW:
            query = query.order_by(desc(ItemModel.item_price))
        elif payload.sort_by == SortBy.NEWEST:
            query = query.order_by(desc(ItemModel.item_created_date))
        elif payload.sort_by == SortBy.OLDEST:
            query = query.order_by(ItemModel.item_created_date)

        if payload.search_input:
            search_input = payload.search_input.lower()
            query = query.filter(
                func.lower(ItemModel.item_name).like(f"{search_input}%")
            )

        # Pagination
        count_query = query
        offset = (payload.page - 1) * payload.limit
        query = query.offset(offset).limit(payload.limit)

        return [query.all(), count_query.count()]

    def get_item_by_id_maintain_session(self, item_id, db) -> ItemModel:
        query = db.query(ItemModel).filter(ItemModel.item_id == item_id)
        return query.first()
