from datetime import datetime
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class ProductDistributor(ConsolidatedBase):
    __tablename__ = 'product_distributor'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    distributor_id: Mapped[str] = mapped_column(String(255))
    sku: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    ean: Mapped[str | None] = mapped_column(String(50))
    category: Mapped[str | None] = mapped_column(String(255))
    maker: Mapped[str | None] = mapped_column(String(255))
    available_in_search: Mapped[str] = mapped_column(String(25))
    stock_quantity: Mapped[int | None] = mapped_column(Integer)
    active: Mapped[str | None] = mapped_column(String(255))
    principle: Mapped[str | None] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
