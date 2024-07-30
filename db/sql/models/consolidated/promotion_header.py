from datetime import datetime
from sqlalchemy import String, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class PromotionHeader(ConsolidatedBase):
    __tablename__ = 'promotion_header'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    distributor_id: Mapped[str] = mapped_column(String(255), ForeignKey('distributor.id', name='fk_promotion_header_distributor'))
    promotion_id: Mapped[str] = mapped_column(String(255))
    title: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(50))
    type: Mapped[str] = mapped_column(String(50))
    price: Mapped[float | None] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    final_price: Mapped[float | None] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    start_date: Mapped[datetime | None] = mapped_column(DateTime)
    end_date: Mapped[datetime | None] = mapped_column(DateTime)
    stop_date: Mapped[datetime | None] = mapped_column(DateTime)
    interval_type: Mapped[str | None] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
