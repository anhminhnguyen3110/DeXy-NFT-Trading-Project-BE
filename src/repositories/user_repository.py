from sqlalchemy.orm import Session

# from schemas.user import UserBase
from models.user_model import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def getByUsername(self, username):
        return self.db.query(User).filter(User.username == username).first()
