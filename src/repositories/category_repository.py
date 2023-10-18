from models.category_model import CategoryModel


class CategoryRepository:
    def get_category_by_id(self, category_id: int, db) -> CategoryModel:
        category = (
            db.query(CategoryModel)
            .filter(CategoryModel.category_id == category_id)
            .first()
        )
        return category

    def get_categories(self, db):
        categories = db.query(CategoryModel).all()
        return categories

    def create_category(
        self, category_name: str, category_description: str, db
    ):
        new_category = CategoryModel(
            category_name=category_name,
            category_description=category_description,
        )

        db.add(new_category)
        db.commit()
