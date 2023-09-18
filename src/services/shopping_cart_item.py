from sqlalchemy.orm import Session
from models.shopping_cart_item_model import (
    ShoppingCartItem,
)  # Import your ShoppingCartItem model
from repositories.shopping_cart_item_repository import (
    ShoppingCartItemRepository,
)  # Import your ShoppingCartItemRepository
from utils.database import get_session


class ShoppingCartItemService:
    def __init__(self):
        self.db = get_session()
        self.shopping_cart_repo = ShoppingCartItemRepository(self.db)

    def get_all(self):
        return None

    def create(self, payload):
        return None
