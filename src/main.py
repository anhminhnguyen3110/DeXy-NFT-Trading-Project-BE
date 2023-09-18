from fastapi import FastAPI
from loguru import logger
from config.core import Setting
from utils.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from routers import (
    shopping_cart_item_router,
    user_router,
    category_router,
    transaction_router,
    item_router,
    offer_router,
)  # Import the transaction_router here
import sys

sys.dont_write_bytecode = True


def create_table():
    logger.debug("Creating Tables")
    Base.metadata.create_all(bind=engine)


def include_router(app: FastAPI):
    logger.debug("Including Routers")
    app.include_router(user_router.router, tags=["User"], prefix="/api/v1")
    app.include_router(
        category_router.router, tags=["Category"], prefix="/api/v1"
    )
    app.include_router(item_router.router, tags=["Item"], prefix="/api/v1")
    app.include_router(
        shopping_cart_item_router.router,
        tags=["Shopping Cart"],
        prefix="/api/v1",
    )
    app.include_router(
        transaction_router.router, tags=["Transaction"], prefix="/api/v1"
    )
    app.include_router(offer_router.router, tags=["Offer"], prefix="/api/v1")


def start_application():
    app = FastAPI(
        title=Setting.PROJECT_NAME,
        version=Setting.PROJECT_VERSION,
    )

    @app.get("/")
    async def test():
        return {"message": "This is the / endpoint"}

    create_table()
    include_router(app)

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = start_application()
