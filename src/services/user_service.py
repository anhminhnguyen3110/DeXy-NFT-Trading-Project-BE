from fastapi import HTTPException, UploadFile
from constants.api_error import ErrorMessages
from repositories.user_repository import UserRepository
from schemas.user.request_dto import CreateUserRequestDto, UpdateUserRequestDto
from schemas.user.response_dto import (
    CreateUserResponseDto,
    GetAnUserResponseDto,
    UpdateUserResponseDto,
)
from utils.parse_image import parse_image_to_base64

from web3 import Web3
from starlette import status


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(
        self, payload: CreateUserRequestDto, db
    ) -> CreateUserResponseDto:
        existing_user = self.user_repo.get_user_by_wallet_address(
            payload.user_wallet_address, db
        )
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.USER_ALREADY_EXISTS,
            )

        self.user_repo.create_user(payload, db)
        return {
            "status": "success",
            "message": "Successfully create a new user user.",
        }

    def get_an_user(self, wallet_address: str, db) -> GetAnUserResponseDto:
        if not Web3.is_address(wallet_address):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed! Wallet address {wallet_address} is not a valid Ethereum address.",
            )
        wallet_address = Web3.to_checksum_address(wallet_address)

        user = self.user_repo.get_user_by_wallet_address(wallet_address, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.USER_NOT_FOUND,
            )
        user_image_base64 = parse_image_to_base64(user.user_image)

        data = {
            "user_id": user.user_id,
            "user_wallet_address": user.user_wallet_address,
            "user_name": user.user_name,
            "user_email": user.user_email,
            "user_image": user_image_base64,
        }

        return GetAnUserResponseDto(data=data)

    def update_an_user(
        self,
        payload: UpdateUserRequestDto,
        user_image: UploadFile,
        user: dict,
        db,
    ) -> UpdateUserResponseDto:
        wallet_address = user["wallet_address"]

        existing_user = self.user_repo.get_user_by_wallet_address(
            wallet_address, db
        )

        if not existing_user:
            raise HTTPException(
                status_code=404, detail=ErrorMessages.USER_NOT_FOUND
            )

        binary_file = None
        if user_image:
            binary_file = user_image.file.read()
            user_image.file.close()

        self.user_repo.update_an_user(wallet_address, payload, binary_file, db)
        return {"status": "success", "message": "Successfully edit user."}
