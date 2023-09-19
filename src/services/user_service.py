from fastapi import HTTPException
from constants.api_error import ErrorMessages
from repositories.user_repository import UserRepository
from schemas.user.request_dto import CreateUserRequestDto
from schemas.user.response_dto import (
    CreateUserResponseDto,
    GetAnUserResponseDto,
)
from utils.database import get_session
from web3 import Web3


class UserService:
    def __init__(self):
        self.db = get_session()
        self.user_repo = UserRepository(self.db)

    def create_user(
        self, payload: CreateUserRequestDto
    ) -> CreateUserResponseDto:
        existing_user = self.user_repo.get_user_by_wallet_address(
            payload.user_wallet_address
        )
        if existing_user:
            raise HTTPException(
                status_code=400, detail=ErrorMessages.USER_ALREADY_EXISTS
            )

        self.user_repo.create_user(payload)
        return CreateUserResponseDto(detail="Success! Create a new user")

    def get_an_user(self, wallet_address: str) -> GetAnUserResponseDto:
        if not Web3.is_address(wallet_address):
            raise HTTPException(
                status_code=422,
                detail=f"Failed! Wallet address {wallet_address} is not a valid Ethereum address.",
            )
        wallet_address = Web3.to_checksum_address(wallet_address)

        existing_user = self.user_repo.get_user_by_wallet_address(
            wallet_address
        )
        if not existing_user:
            raise HTTPException(
                status_code=404, detail=ErrorMessages.USER_NOT_FOUND
            )
        data = {
            "user_id": existing_user.user_id,
            "user_wallet_address": existing_user.user_wallet_address,
            "user_name": existing_user.user_name,
            "user_email": existing_user.user_email,
            "user_image": existing_user.user_image,
        }

        return GetAnUserResponseDto(data=data)

    def update_an_user(
        self, wallet_address, user_name: str, user_email: str, user_image
    ):
        if not Web3.is_address(wallet_address):
            raise HTTPException(
                status_code=422,
                detail=f"Failed! Wallet address {wallet_address} is not a valid Ethereum address.",
            )
        wallet_address = Web3.to_checksum_address(wallet_address)

        existing_user = self.user_repo.get_user_by_wallet_address(
            wallet_address
        )
        if not existing_user:
            raise HTTPException(
                status_code=404, detail=ErrorMessages.USER_NOT_FOUND
            )
        if user_image:
            binary_file = user_image.file.read()
            user_image.file.close()
        self.user_repo.update_an_user(
            wallet_address, user_name, user_email, binary_file
        )
        return {"status": "success", "message": "Successfully edit user."}
