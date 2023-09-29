from sqlalchemy import Column, Integer, String
from utils.database import BaseModel
from sqlalchemy.orm import relationship, Mapped


class CategoryModel(BaseModel):
    __tablename__ = "Categories"

    category_id = Column(Integer, primary_key=True, nullable=False)  # Index
    category_description = Column(String(255))
    category_name = Column(String(20), nullable=False)

    items = relationship("ItemModel", back_populates="category")

    def __init__(
        self, category_id: int, category_description: str, category_name: str
    ):
        self.category_id = category_id
        self.category_description = category_description
        self.category_name = category_name
