from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from utils.database import BaseModel
from datetime import date


class Transaction(BaseModel):
    __tablename__ = "Transactions"

    transaction_id = Column(Integer, primary_key=True, nullable=False)
    transaction_event = Column(Integer, nullable=False)
    transaction_item_name = Column(Integer, nullable=False)
    transaction_price = Column(Integer, nullable=False)
    transaction_from_user_id = Column(
        Integer, ForeignKey("Users.user_id"), nullable=False
    )
    transaction_to_user_id = Column(
        Integer, ForeignKey("Users.user_id"), nullable=False
    )
    transaction_date = Column(Date, nullable=False)

    from_user = relationship("User", back_populates="transactions_sent")
    to_user = relationship("User", back_populates="transactions_received")

    def __init__(
        self,
        transaction_event: str,
        transaction_item_name: str,
        transaction_price: float,
        transaction_from_user_id: int,
        transaction_to_user_id: int,
        transaction_date: date,
    ):
        self.transaction_event = transaction_event
        self.transaction_item_name = transaction_item_name
        self.transaction_price = transaction_price
        self.transaction_from_user_id = transaction_from_user_id
        self.transaction_to_user_id = transaction_to_user_id
        self.transaction_date = transaction_date
