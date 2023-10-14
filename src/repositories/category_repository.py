from models.category_model import CategoryModel
from sqlalchemy.orm import Session


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_category_by_id(self, category_id: int) -> CategoryModel:
        category = (
            self.db.query(CategoryModel)
            .filter(CategoryModel.category_id == category_id)
            .first()
        )
        self.db.close()
        return category

    def get_categories(self):
        categories = self.db.query(CategoryModel).all()
        self.db.close()
        return categories

    def create_category(self, category_name: str, category_description: str):
        new_category = CategoryModel(
            category_name=category_name,
            category_description=category_description,
        )

        self.db.add(new_category)
        self.db.commit()
        self.db.close()
