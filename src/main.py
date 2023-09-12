from fastapi import FastAPI
from loguru import logger
from config.core import Setting
from utils.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

from routers import user_router


def create_table():
  logger.debug('Creating Tables')
  Base.metadata.create_all(bind=engine)
  
def include_router(app: FastAPI):
  logger.debug('Including Routers')
  app.include_router(user_router.router, tags=['user'])
  
def start_application():
  app = FastAPI(
    title = Setting.PROJECT_NAME,
    version = Setting.PROJECT_VERSION,
    root_path=Setting.API_ROOT_PATH,
  )
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