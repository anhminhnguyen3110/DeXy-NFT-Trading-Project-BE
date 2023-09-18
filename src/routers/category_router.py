from abc import ABC
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from utils.database import get_session

# from schemas.category.request_dto import CategoryCreate  # Import your CategoryCreate schema here
from services.category_service import (
    CategoryService,
)  # Import your CategoryService here

router = APIRouter()


@cbv(router)
class CategoryRouter:
    session: Session = Depends(get_session)

    @router.get("/categories")
    def get_all(self):
        return CategoryService.get_all(self.session)

    @router.get("/categories/{id}")
    def get_by_id(self, id: int):
        return CategoryService.get_by_id(self.session, id)

    @router.post("/categories")
    def create_category(self, payload):
        return CategoryService.create(self.session, payload)

    @router.put("/categories/{id}")
    def update_category(self, id: int, payload):
        return CategoryService.update(self.session, id, payload)

    @router.delete("/categories/{id}")
    def delete_category(self, id: int):
        return CategoryService.delete_by_id(self.session, id)
