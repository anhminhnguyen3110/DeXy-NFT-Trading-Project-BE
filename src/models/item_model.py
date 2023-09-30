from typing import List
from sqlalchemy import (
    Column,
    Integer,
    String,
    LargeBinary,
    Float,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship, Mapped
from utils.database import BaseModel
from datetime import datetime


class ItemModel(BaseModel):
    __tablename__ = "Items"

    item_id = Column(
        Integer, primary_key=True, nullable=False, index=True
    )  # Index
    item_name = Column(String(20), nullable=False, index=True)  # Index
    item_owner_id = Column(Integer, ForeignKey("Users.user_id"), nullable=False)
    item_image = Column(LargeBinary(length=(2**32) - 1), nullable=True)
    item_description = Column(String(50))
    item_category_id = Column(
        Integer,
        ForeignKey("Categories.category_id"),
        nullable=False,
    )
    item_price = Column(Float, nullable=False)
    item_price_currency = Column(String(50), nullable=False)
    item_created_date = Column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    item_created_by_address = Column(String(50), nullable=False)

    user = relationship("UserModel", back_populates="items")
    category = relationship("CategoryModel", back_populates="items")
    shopping_cart_item = relationship(
        "ShoppingCartItemModel", back_populates="item"
    )
    offers = relationship("OfferModel", back_populates="item")

    def __init__(
        self,
        item_name: str,
        item_owner_id: int,
        item_category_id: int,
        item_price: int,
        item_price_currency: str,
        item_created_by_address: str,
        item_description: str = None,
        item_image: str = None,
    ):
        self.item_name = item_name
        self.item_owner_id = item_owner_id
        self.item_category_id = item_category_id
        self.item_price = item_price
        self.item_price_currency = item_price_currency
        self.item_description = item_description
        self.item_image = item_image
        self.item_created_by_address = item_created_by_address
