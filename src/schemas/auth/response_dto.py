from pydantic import BaseModel, Field


class ConnectWalletResponseDto(BaseModel):
    access_token: str = Field(
        ...,
        example="token",
        description="Access token for authentication",
        type="string",
    )
    token_type: str = Field(
        ...,
        example="bearer",
        description="Type of the access token (e.g., 'bearer')",
        type="string",
    )
