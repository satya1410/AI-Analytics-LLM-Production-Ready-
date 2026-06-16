from datetime import date

from sqlalchemy import (
    String,
    Float,
    Integer,
    Date,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.models.base import Base


class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    customer_id: Mapped[str] = mapped_column(
        ForeignKey("customers.customer_id")
    )

    product_id: Mapped[str] = mapped_column(
        ForeignKey("products.product_id")
    )

    order_date: Mapped[date] = mapped_column(Date)

    sales: Mapped[float] = mapped_column(Float)
    profit: Mapped[float] = mapped_column(Float)
    discount: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(Integer)

    customer = relationship("Customer")
    product = relationship("Product")