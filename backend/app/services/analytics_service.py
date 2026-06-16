from sqlalchemy import func

from app.models.order import Order
from app.models.product import Product


class AnalyticsService:

    def __init__(self, db):
        self.db = db

    def top_products(self, limit: int = 10):

        return (
            self.db.query(
                Product.product_name,
                func.sum(Order.profit).label("total_profit")
            )
            .join(
                Product,
                Product.product_id == Order.product_id
            )
            .group_by(Product.product_name)
            .order_by(
                func.sum(Order.profit).desc()
            )
            .limit(limit)
            .all()
        )