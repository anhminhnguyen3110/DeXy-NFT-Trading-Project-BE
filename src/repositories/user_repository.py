from sqlalchemy import func
from sqlalchemy.orm import Session
from models.user_model import UserModel
from schemas.user.request_dto import CreateUserRequestDto, UpdateUserRequestDto
from datetime import datetime

from schemas.search.request_dto import SearchRequestDto


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_wallet_address(self, wallet_address: str) -> UserModel:
        user = (
            self.db.query(UserModel)
            .filter(UserModel.user_wallet_address == wallet_address)
            .first()
        )

        self.db.close()
        return user

    def create_user(self, payload: CreateUserRequestDto) -> UserModel:
        user = UserModel(
            user_wallet_address=payload.user_wallet_address,
            user_name="Default Name",
        )
        self.db.add(user)
        self.db.commit()
        self.db.close()

        return user

    def update_an_user(
        self, wallet_address, payload: UpdateUserRequestDto, user_image
    ) -> None:
        user = self.get_user_by_wallet_address(wallet_address)
        if payload.user_name:
            user.user_name = payload.user_name
        if payload.user_email:
            user.user_email = payload.user_email
        if user_image:
            user.user_image = user_image
        user.updated_at = datetime.now()
        self.db.commit()
        self.db.refresh(user)
        self.db.close()

    def search_users(self, payload: SearchRequestDto):
        page = payload.page
        limit = payload.limit
        search_input = payload.search_input.lower()

        query = self.db.query(UserModel).filter(
            func.lower(UserModel.user_name).like(f"{search_input}%")
        )
        users_count = query.count()
        users = query.offset((page - 1) * limit).limit(limit).all()

        self.db.close()
        return [users, users_count]
