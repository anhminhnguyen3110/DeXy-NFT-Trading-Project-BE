from sqlalchemy.orm import Session
from models.user_model import UserModel
from schemas.user.request_dto import CreateUserRequestDto
from datetime import datetime


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_wallet_address(self, wallet_address: str) -> UserModel:
        return (
            self.db.query(UserModel)
            .filter(UserModel.user_wallet_address == wallet_address)
            .first()
        )

    def create_user(self, payload: CreateUserRequestDto):
        user = UserModel(
            user_wallet_address=payload.user_wallet_address,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

    def update_an_user(
        self, wallet_address, user_name: str, user_email: str, user_image
    ):
        user = self.get_user_by_wallet_address(wallet_address)
        if user_name:
            user.user_name = user_name
        if user_email:
            user.user_email = user_email
        if user_image:
            user.user_image = user_image
        user.updated_at = datetime.now()
        self.db.commit()
        self.db.refresh(user)
