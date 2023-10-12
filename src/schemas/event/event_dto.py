from pydantic import BaseModel


class TransactionItem(BaseModel):
    transactionId: int
    item: int
    buyer: str
    owner: str
