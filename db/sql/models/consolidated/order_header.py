from datetime import datetime
from sqlalchemy import String, Integer, Boolean, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class OrderHeader(ConsolidatedBase):
    __tablename__ = 'order_header'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    distributor_id: Mapped[str] = mapped_column(String(255), ForeignKey('distributor.id', name='fk_order_header_distributor'))
    order_id: Mapped[int] = mapped_column(Integer)
    client_id: Mapped[str] = mapped_column(String(255), ForeignKey('client.id', name='fk_order_header_client'))
    user_id: Mapped[str | None] = mapped_column(String(255), ForeignKey('user.id', name='fk_order_header_user'))
    user_role: Mapped[str] = mapped_column(String(50))
    branch: Mapped[str] = mapped_column(String(255))
    warehouse: Mapped[str] = mapped_column(String(255))
    state_from: Mapped[str | None] = mapped_column(String(2))
    state_to: Mapped[str | None] = mapped_column(String(2))
    payment_condition: Mapped[str | None] = mapped_column(String(255))
    payment_method: Mapped[str | None] = mapped_column(String(100))
    medium_term: Mapped[int | None] = mapped_column(Integer)
    instalments: Mapped[int | None] = mapped_column(Integer)
    payment_status: Mapped[str | None] = mapped_column(String(255))
    order_status: Mapped[str] = mapped_column(String(255))
    origin: Mapped[str] = mapped_column(String(50))
    # app_mobile_nexfar: Mapped[bool] = mapped_column(Boolean)
    device: Mapped[str] = mapped_column(String(50))
    total: Mapped[float | None] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    total_with_taxes: Mapped[float | None] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    original_order_total: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    original_order_total_with_taxes: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    total_after_return: Mapped[float | None] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    total_with_taxes_after_return: Mapped[float | None] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
