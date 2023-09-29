from sqlalchemy import Column, Integer, String, LargeBinary
from utils.database import BaseModel
from sqlalchemy.orm import relationship, Mapped
from typing import List


class UserModel(BaseModel):
    __tablename__ = "Users"

    user_id = Column(
        Integer, primary_key=True, index=True, autoincrement=True
    )  # Index
    user_name = Column(String(50), nullable=True, index=True)  # Index
    user_wallet_address = Column(
        String(50), nullable=False, index=True, unique=True
    )  # Index
    user_image = Column(LargeBinary(length=(2**32) - 1), nullable=True)
    user_email = Column(String(50), nullable=True)

    items = relationship("ItemModel", back_populates="user")
    transactions_sent = relationship(
        "TransactionModel",
        back_populates="from_user",
        primaryjoin="UserModel.user_id == TransactionModel.transaction_from_user_id",
    )
    transactions_received = relationship(
        "TransactionModel",
        back_populates="to_user",
        primaryjoin="UserModel.user_id == TransactionModel.transaction_to_user_id",
    )
    shopping_cart_items = relationship(
        "ShoppingCartItemModel", back_populates="user"
    )
    offers = relationship("OfferModel", back_populates="user")

    def __init__(
        self,
        user_wallet_address: str,
        user_email: str = None,
        user_name: str = None,
        user_image: str = None,
    ):
        self.user_name = user_name
        self.user_wallet_address = user_wallet_address
        self.user_email = user_email
        self.user_image = user_image

    def __repr__(self):
        return f"<User {self.user_name}> {self.user_wallet_address} {self.user_email}"
