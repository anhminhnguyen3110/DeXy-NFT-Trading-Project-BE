from sqlalchemy.orm import Session
from models.offer_model import Offer  # Import your Offer model here


class OfferRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_name(self):
        return None
