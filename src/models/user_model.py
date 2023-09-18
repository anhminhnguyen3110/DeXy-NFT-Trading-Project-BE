from sqlalchemy import Column, Integer, String, LargeBinary
from utils.database import BaseModel
from sqlalchemy.orm import relationship


class User(BaseModel):
    __tablename__ = "Users"

    user_id = Column(
        Integer, primary_key=True, index=True, autoincrement=True
    )  # Index
    user_name = Column(String(50), nullable=False)
    user_wallet_address = Column(
        String(50), nullable=False, index=True, unique=True
    )  # Index
    user_image = Column(LargeBinary)
    user_email = Column(String(50))

    items = relationship("Items", back_populates="owner")
    transactions = relationship("Transactions", back_populates="owner")
    shopping_cart_items = relationship(
        "ShoppingCartItem", back_populates="user"
    )
    offers = relationship("Offer", back_populates="user")

    def __init__(
        self,
        user_name: str,
        user_wallet_address: str,
        user_email: str,
        user_image: str,
    ):
        self.user_name = user_name
        self.user_wallet_address = user_wallet_address
        self.user_email = user_email
        self.user_image = user_image
