from abc import ABC
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from repositories.item_repository import ItemRepository
from models.item_model import Item
from utils.database import get_session
from services.shopping_cart_item import ShoppingCartItemService

router = APIRouter()


@cbv(router)
class ShoppingCartItemRouter:
    session: Session = Depends(get_session)

    @router.get("/items")
    def get_all(self):
        return None
