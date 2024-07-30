from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class Product(ConsolidatedBase):
    __tablename__ = 'product'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    ean: Mapped[str] = mapped_column(String(50))
    maker: Mapped[str] = mapped_column(String(255))
    main_category: Mapped[str] = mapped_column(String(255))
    secondary_categories: Mapped[str | None] = mapped_column(String)
    principle: Mapped[str | None] = mapped_column(String)
    data_source: Mapped[str | None] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
