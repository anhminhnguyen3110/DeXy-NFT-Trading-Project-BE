from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from utils.database import BaseModel


class ShoppingCartItem(BaseModel):
    __tablename__ = "Shopping_cart_items"

    shopping_cart_item_id = Column(Integer, primary_key=True, nullable=False)
    shopping_cart_item_user_id = Column(
        Integer, ForeignKey("Users.user_id"), nullable=False
    )
    item_id = Column(Integer, ForeignKey("Items.item_id"), nullable=False)

    # Define a relationship to the User model (Shopping cart owner)
    user = relationship("User", back_populates="shopping_cart_items")

    # Define a relationship to the Item model (Shopping cart item)
    item = relationship("Item", back_populates="shopping_cart_items")

    def __init__(self, shopping_cart_item_user_id: int, item_id: int):
        self.shopping_cart_item_user_id = shopping_cart_item_user_id
        self.item_id = item_id
