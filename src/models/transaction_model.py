from sqlalchemy import Column, Integer, ForeignKey, Date, Double
from sqlalchemy.orm import relationship, Mapped
from utils.database import BaseModel
from datetime import date


class TransactionModel(BaseModel):
    __tablename__ = "Transactions"

    transaction_id = Column(Integer, primary_key=True, nullable=False)

    transaction_smart_contract_id = Column(Integer, nullable=False)

    transaction_user_id = Column(
        Integer, ForeignKey("Users.user_id"), nullable=False
    )

    user = relationship(
        "UserModel",
        primaryjoin="UserModel.user_id == TransactionModel.transaction_user_id",
        back_populates="transactions",
    )

    def __init__(
        self,
        transaction_smart_contract_id: int,
        transaction_user_id: int,
    ):
        self.transaction_smart_contract_id = transaction_smart_contract_id
        self.transaction_user_id = transaction_user_id
