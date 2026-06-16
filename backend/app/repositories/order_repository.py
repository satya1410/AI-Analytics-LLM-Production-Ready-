from sqlalchemy.orm import Session

from app.models.order import Order


class OrderRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Order).all()

    def get_by_id(self, order_id: str):
        return (
            self.db.query(Order)
            .filter(Order.order_id == order_id)
            .first()
        )

    def count(self):
        return self.db.query(Order).count()