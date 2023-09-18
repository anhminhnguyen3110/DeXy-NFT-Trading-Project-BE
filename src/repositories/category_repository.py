from sqlalchemy.orm import Session
from models.category_model import Category  # Import your Category model here


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_name(self, category_name):
        return (
            self.db.query(Category)
            .filter(Category.category_name == category_name)
            .first()
        )
