from pydantic import BaseModel, Field
from typing import Optional


class CreateUserResponseDto(BaseModel):
    status: str = Field(..., example="Success")
    message: str = Field(..., example="Create a new user successfully!")


class UpdateUserResponseDto(BaseModel):
    status: str = Field(..., example="Success")
    message: str = Field(..., example="Update an user successfully!")


class SubGetAnUserResponseDto(BaseModel):
    user_id: int
    user_name: Optional[str] = None
    user_wallet_address: str
    user_image: Optional[bytes] = None
    user_email: Optional[str] = None


class GetAnUserResponseDto(BaseModel):
    data: SubGetAnUserResponseDto
