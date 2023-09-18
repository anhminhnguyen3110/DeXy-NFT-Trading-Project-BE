from sqlalchemy.orm import Session
from models.category_model import Category
from repositories.category_repository import CategoryRepository
from utils.database import get_session


class CategoryService:
    def __init__(self):
        self.db = get_session()
        self.category_repo = CategoryRepository(self.db)

    def get_all(self) -> list[Category]:
        return self.category_repo.get_all()

    def get_by_id(self, id: int) -> Category:
        return self.category_repo.get_by_id(id)

    def create(self, payload) -> Category:
        return self.category_repo.create_category(
            category_id=payload.category_id,
            category_description=payload.category_description,
            category_name=payload.category_name,
        )

    def update(self, id: int, payload) -> Category:
        return self.category_repo.update_category(
            category_id=id,
            category_description=payload.category_description,
            category_name=payload.category_name,
        )

    def delete_by_id(self, id: int):
        return self.category_repo.delete_category(id)
