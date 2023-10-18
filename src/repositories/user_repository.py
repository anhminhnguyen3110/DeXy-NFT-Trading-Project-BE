from sqlalchemy import func
from sqlalchemy.orm import Session
from models.user_model import UserModel
from schemas.user.request_dto import CreateUserRequestDto, UpdateUserRequestDto
from datetime import datetime

from schemas.search.request_dto import SearchRequestDto


class UserRepository:
    def get_user_by_wallet_address(self, wallet_address: str, db) -> UserModel:
        user = (
            db.query(UserModel)
            .filter(UserModel.user_wallet_address == wallet_address)
            .first()
        )

        return user

    def create_user(self, payload: CreateUserRequestDto, db) -> UserModel:
        user = UserModel(
            user_wallet_address=payload.user_wallet_address,
            user_name="Default Name",
        )
        db.add(user)
        db.commit()
        new_user = self.get_user_by_wallet_address(payload.user_wallet_address, db)

        return new_user

    def update_an_user(
        self, wallet_address, payload: UpdateUserRequestDto, user_image, db
    ) -> None:
        user = self.get_user_by_wallet_address(wallet_address, db)
        if payload.user_name:
            user.user_name = payload.user_name
        if payload.user_email:
            user.user_email = payload.user_email
        if user_image:
            user.user_image = user_image
        user.updated_at = datetime.now()
        db.commit()
        db.refresh(user)

    def search_users(self, payload: SearchRequestDto, db):
        page = payload.page
        limit = payload.limit
        search_input = payload.search_input.lower()

        query = db.query(UserModel).filter(
            func.lower(UserModel.user_name).like(f"{search_input}%")
        )
        users_count = query.count()
        users = query.offset((page - 1) * limit).limit(limit).all()

        return [users, users_count]
