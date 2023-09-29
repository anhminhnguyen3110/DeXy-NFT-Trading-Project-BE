from sqlalchemy import func
from sqlalchemy.orm import Session
from models.user_model import UserModel
from schemas.user.request_dto import CreateUserRequestDto
from datetime import datetime

from schemas.search.request_dto import SearchRequestDto
from constants.pagination import SortBy


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_wallet_address(self, wallet_address: str) -> UserModel:
        return (
            self.db.query(UserModel)
            .filter(UserModel.user_wallet_address == wallet_address)
            .first()
        )

    def create_user(self, payload: CreateUserRequestDto) -> UserModel:
        user = UserModel(
            user_wallet_address=payload.user_wallet_address,
            user_name="Default Name",
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_an_user(
        self, wallet_address, user_name: str, user_email: str, user_image
    ) -> None:
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

    def search_users(self, payload: SearchRequestDto) -> list[UserModel]:
        page = payload.page
        limit = payload.limit
        search_input = payload.search_input.lower()

        query = self.db.query(UserModel).filter(
            func.lower(UserModel.user_name).like(f"{search_input}%")
        )

        users = query.offset((page - 1) * limit).limit(limit).all()

        return users
