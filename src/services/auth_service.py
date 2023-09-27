from fastapi import HTTPException
from config.core import Setting
from constants.api_error import ErrorMessages
from repositories.user_repository import UserRepository
from schemas.auth.request_dto import ConnectWalletRequestDto
from schemas.auth.response_dto import ConnectWalletResponseDto
from schemas.user.request_dto import CreateUserRequestDto
from utils.auth import create_access_token
from utils.database import get_session
from utils.web3 import Web3Service
from starlette import status


class AuthService:
    def __init__(self):
        self.db = get_session()
        self.user_repo = UserRepository(self.db)
        pass

    def connect_wallet(
        self, payload: ConnectWalletRequestDto
    ) -> ConnectWalletResponseDto:
        existing_user = self.user_repo.get_user_by_wallet_address(
            payload.wallet_address
        )
        if existing_user == None:
            new_user = self.user_repo.create_user(
                CreateUserRequestDto(user_wallet_address=payload.wallet_address)
            )
            existing_user = new_user

        if not self.validate_signature(
            payload.wallet_address, payload.signature
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.INVALID_SIGNATURE,
            )
        access_token = create_access_token(
            {
                "wallet_address": existing_user.user_wallet_address,
                "user_id": existing_user.user_id,
            }
        )
        return ConnectWalletResponseDto(
            access_token=access_token, token_type="bearer"
        )

    def validate_signature(self, address: str, signature: str) -> bool:
        checksum_address = Web3Service.to_checksum_address(address)
        checksum_recover = Web3Service.recover(
            message=Setting.SIGN_MESSAGE_TO_LOGIN, signature=signature
        )

        return checksum_address == checksum_recover
