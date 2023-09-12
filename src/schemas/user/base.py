from typing import Optional
from pydantic import BaseModel, Field

class UserBase(BaseModel):
  name: str
  user_address: str = Field(max_length=50)