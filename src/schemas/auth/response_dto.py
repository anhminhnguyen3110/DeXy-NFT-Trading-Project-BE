from pydantic import BaseModel, Field


class ConnectWalletResponseDto(BaseModel):
    access_token: str = Field(..., example="token")
    token_type: str = Field(..., example="bearer")
