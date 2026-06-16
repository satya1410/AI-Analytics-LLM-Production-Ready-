from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    category: Mapped[str] = mapped_column(String)
    sub_category: Mapped[str] = mapped_column(String)
    product_name: Mapped[str] = mapped_column(String)