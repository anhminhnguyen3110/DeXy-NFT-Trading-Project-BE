from fastapi import FastAPI
from loguru import logger
from config.core import Setting
from utils.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from routers import (
    auth_router,
    user_router,
    item_router,
    search_router,
    # transaction_router,
    # offer_router,
)  # Import the transaction_router here
import sys
from models import (
    shopping_cart_item_model,
    user_model,
    category_model,
    transaction_model,
    item_model,
    offer_model,
)  # Import the transaction_model here

sys.dont_write_bytecode = True


def create_table():
    logger.debug("Creating Tables")
    Base.metadata.create_all(bind=engine)


def include_router(app: FastAPI):
    logger.debug("Including Routers")
    app.include_router(user_router.router, prefix="/api/v1")
    app.include_router(item_router.router, prefix="/api/v1")
    app.include_router(auth_router.router, prefix="/api/v1")
    app.include_router(search_router.router, prefix="/api/v1")


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
