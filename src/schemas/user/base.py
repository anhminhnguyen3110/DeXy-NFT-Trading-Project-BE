from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str
    user_wallet_address: str
