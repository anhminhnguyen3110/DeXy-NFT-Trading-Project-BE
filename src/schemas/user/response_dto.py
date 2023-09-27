from pydantic import BaseModel, Field
from typing import Optional


class BaseResponseDto(BaseModel):
    status: str = Field(
        ...,
        example="Success",
        description="Status of the response",
        type="string",
    )
    message: str = Field(
        ...,
        example="Operation successful!",
        description="Description of the response message",
        type="string",
    )


class SubGetAnUserResponseDto(BaseModel):
    user_id: int = Field(
        ..., example=123, description="ID of the user", type="integer"
    )
    user_name: Optional[str] = Field(
        None, example="John Doe", description="Name of the user", type="string"
    )
    user_wallet_address: str = Field(
        ...,
        example="0xabcdef1234567890",
        description="Wallet address of the user",
        type="string",
    )
    user_image: Optional[bytes] = Field(
        None,
        example="base64-encoded-image",
        description="Image data of the user",
        type="string",  # Assuming this is a base64-encoded image
    )
    user_email: Optional[str] = Field(
        None,
        example="user@example.com",
        description="Email address of the user",
        type="string",
    )


class CreateUserResponseDto(BaseResponseDto):
    pass


class UpdateUserResponseDto(BaseResponseDto):
    pass


class GetAnUserResponseDto(BaseModel):
    data: SubGetAnUserResponseDto
