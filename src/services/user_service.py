from sqlalchemy.orm import Session
from models.user_model import User
from repositories.user_repository import UserRepository
from utils.database import get_session


class UserService:
    def __init__(self):
        self.db = get_session()
        self.user_repo = UserRepository(self.db)

    def get_all(self) -> list[User]:
        return self.user_repo.get_all()

    def get_by_id(self, id: int) -> User:
        return self.user_repo.get_by_id(id)

    def get_by_username(self, username: str) -> User:
        return self.user_repo.get_by_username(username)

    def create(self, user_data) -> User:
        return self.user_repo.create_user(
            user_name=user_data.user_name,
            user_wallet_address=user_data.user_wallet_address,
            user_email=user_data.user_email,
            user_image=user_data.user_image,
        )

    def update(self, id: int, user_data) -> User:
        return self.user_repo.update_user(
            user_id=id,
            user_name=user_data.user_name,
            user_wallet_address=user_data.user_wallet_address,
            user_email=user_data.user_email,
            user_image=user_data.user_image,
        )

    def delete_by_id(self, id: int):
        return self.user_repo.delete_user(id)
