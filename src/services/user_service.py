from fastapi import HTTPException
from constants.api_error import ErrorMessages
from repositories.user_repository import UserRepository
from schemas.user.request_dto import CreateUserRequestDto
from schemas.user.response_dto import (
    CreateUserResponseDto,
    GetAnUserResponseDto,
    UpdateUserResponseDto,
)
from utils.database import get_session
from web3 import Web3
import base64
from starlette import status


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
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.USER_ALREADY_EXISTS,
            )

        self.user_repo.create_user(payload)
        return {
            "status": "success",
            "message": "Successfully create a new user user.",
        }

    def get_an_user(self, wallet_address: str) -> GetAnUserResponseDto:
        if not Web3.is_address(wallet_address):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed! Wallet address {wallet_address} is not a valid Ethereum address.",
            )
        wallet_address = Web3.to_checksum_address(wallet_address)

        user = self.user_repo.get_user_by_wallet_address(wallet_address)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.USER_NOT_FOUND,
            )
        user_image_base64 = None
        if user.user_image:
            user_image_base64 = base64.b64encode(user.user_image).decode(
                "utf-8"
            )

        data = {
            "user_id": user.user_id,
            "user_wallet_address": user.user_wallet_address,
            "user_name": user.user_name,
            "user_email": user.user_email,
            "user_image": user_image_base64,
        }

        return GetAnUserResponseDto(data=data)

    def update_an_user(
        self, wallet_address, user_name: str, user_email: str, user_image
    ) -> UpdateUserResponseDto:
        if not Web3.is_address(wallet_address):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
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

        binary_file = None
        if user_image:
            binary_file = user_image.file.read()
            user_image.file.close()

        self.user_repo.update_an_user(
            wallet_address, user_name, user_email, binary_file
        )
        return {"status": "success", "message": "Successfully edit user."}
