from pydantic import BaseModel, Field
from typing import Optional


class CreateUserResponseDto(BaseModel):
    detail: str = Field(..., example="Success! Create a new user")


class SubGetAnUserResponseDto(BaseModel):
    user_id: int
    user_name: Optional[str] = None
    user_wallet_address: str
    user_image: Optional[bytes] = None
    user_email: Optional[str] = None


class GetAnUserResponseDto(BaseModel):
    data: SubGetAnUserResponseDto
