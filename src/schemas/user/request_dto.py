from typing import Optional
from pydantic import BaseModel, Field
from schemas.user.base import UserBase


class UserCreate(UserBase):
    pass
