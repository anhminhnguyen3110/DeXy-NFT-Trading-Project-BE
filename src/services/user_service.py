from sqlalchemy.orm import Session
from models.user import User
from repositories.user_repository import UserRepository
from utils.database import get_session

class UserService: 
  def __init__(self):
    self.db = get_session()
    self.user_repo = UserRepository(self.db)
  
  def get_all(session: Session) -> list[User]:
    return None
  
  def get_by_id(session: Session) -> User:
    return None

  def getByUsername(self, username):
    return self.user_repo.getByUsername(username)
  
  def create(session: Session) -> int:
    return None

  
  def update(session: Session) -> int:
    return None

  
  def delete_by_id(session: Session):
    return None
  