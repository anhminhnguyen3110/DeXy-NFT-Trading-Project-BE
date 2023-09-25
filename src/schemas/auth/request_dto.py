from pydantic import BaseModel, Field, validator
from fastapi import HTTPException
from utils.web3 import Web3Service
from starlette import status


class ConnectWalletRequestDto(BaseModel):
    wallet_address: str = Field(
        ...,
        example="0x1aBA989D0703cE6CC651B6109d02b39a9651aE5d",
        description="Wallet address of the user",
        type="string",
    )

    signature: str = Field(
        ...,
        example="0x869b7252e1b74e0ebabe055f69341b3ec0af023a0608ed4fdcb536f965337eda1c95b788019efcacea4275ed348db7749c6101de11f844e08910e70c5ab244ec1b",
        description="Signature of the user",
        type="string",
    )

    @validator("wallet_address")
    def validate_wallet_address(cls, value: str) -> str:
        if not Web3Service.is_address(value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Failed! Wallet address {value} is not a valid Ethereum address.",
            )
        checksum_address = Web3Service.to_checksum_address(value)
        return checksum_address
