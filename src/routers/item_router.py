from abc import ABC
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from repositories.item_repository import (
    ItemRepository,
)  # Import your ItemRepository here

# from schemas.item.request_dto import ItemCreate  # Import your ItemCreate schema here
from models.item_model import Item  # Import your Item model here
from utils.database import get_session

router = APIRouter()


@cbv(router)
class ItemRouter:
    session: Session = Depends(get_session)
    item_repo = ItemRepository(session)

    @router.get("/items")
    def get_all(self):
        items = self.item_repo.get_all()
        return items

    @router.get("/items/{item_id}")
    def get_by_id(self, item_id: int):
        item = self.item_repo.get_by_id(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.post("/items")
    def create_item(self):
        item = self.item_repo.create_item(
            item_name=payload.item_name,
            item_owner_id=payload.item_owner_id,
            item_category_id=payload.item_category_id,
            item_price=payload.item_price,
            item_price_currency=payload.item_price_currency,
            item_created_by_address=payload.item_created_by_address,
            item_description=payload.item_description,
            item_image=payload.item_image,
        )
        return item

    @router.put("/items/{item_id}")
    def update(self, item_id: int, payload):
        item = self.item_repo.update_item(
            item_id=item_id,
            item_name=payload.item_name,
            item_owner_id=payload.item_owner_id,
            item_category_id=payload.item_category_id,
            item_price=payload.item_price,
            item_price_currency=payload.item_price_currency,
            item_created_by_address=payload.item_created_by_address,
            item_description=payload.item_description,
            item_image=payload.item_image,
        )
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.delete("/items/{item_id}")
    def delete_by_id(self, item_id: int):
        success = self.item_repo.delete_item(item_id)
        if not success:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"message": "Item deleted"}
