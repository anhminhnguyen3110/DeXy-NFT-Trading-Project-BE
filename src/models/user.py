from sqlalchemy import Column, String
from utils.database import BaseModel

class User(BaseModel):
  __tablename__ = 'user'
  
  name = Column(String(255), nullable=False, index = True)
  
  wallet_address = Column(String(50), nullable=False, index = True)
  
  def __init__(self, name, wallet_address) -> None:
    self.name = name
    self.wallet_address = wallet_address
  
  def __repr__(self) -> str:
    return f'<User(name={self.name}, wallet_address={self.wallet_address})>'