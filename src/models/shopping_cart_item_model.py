from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from utils.database import BaseModel


class ShoppingCartItemModel(BaseModel):
    __tablename__ = "ShoppingCartItems"

    shopping_cart_item_id = Column(
        Integer, primary_key=True, nullable=False
    )  # Index
    shopping_cart_item_user_id = Column(
        Integer, ForeignKey("Users.user_id"), nullable=False
    )
    shopping_cart_item_item_id = Column(
        Integer, ForeignKey("Items.item_id"), nullable=False
    )

    user = relationship("UserModel", back_populates="shopping_cart_items")
    item = relationship("ItemModel", back_populates="shopping_cart_item")

    def __init__(
        self, shopping_cart_item_user_id: int, shopping_cart_item_item_id: int
    ):
        self.shopping_cart_item_user_id = shopping_cart_item_user_id
        self.shopping_cart_item_item_id = shopping_cart_item_item_id
