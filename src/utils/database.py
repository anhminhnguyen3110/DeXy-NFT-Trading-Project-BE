from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.core import Setting
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

engine = create_engine(
    url=Setting.DB_CONNECTION_STR,
    echo=False,
    pool_recycle=7200,
    pool_pre_ping=True,
)  # echo = show-sql
Session = sessionmaker(bind=engine, autoflush=True, autocommit=False)

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    server_created_at = Column(
        DateTime, server_default=func.now()
    )  # created record server time at
    server_updated_at = Column(
        DateTime, onupdate=func.now()
    )  # updated record server time at


def get_session():
    try:
        session = Session()
        return session
    finally:
        session.close()
