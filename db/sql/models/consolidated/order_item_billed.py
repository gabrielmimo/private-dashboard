from datetime import datetime
from sqlalchemy import String, Integer, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class OrderItemBilled(ConsolidatedBase):
    __tablename__ = 'order_item_billed'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    order_header_id: Mapped[str] = mapped_column(String(255), ForeignKey('order_header.id', name='fk_order_item_billed_order_header'))
    product_distributor_id: Mapped[str] = mapped_column(String(255))
    product_id: Mapped[str | None] = mapped_column(String(255), ForeignKey('product.id', name='order_item_billed_fk'))
    ean: Mapped[str | None] = mapped_column(String(50))
    quantity_requested: Mapped[int] = mapped_column(Integer)
    quantity_attended: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    final_price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    sub_total: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    sub_total_with_taxes: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
