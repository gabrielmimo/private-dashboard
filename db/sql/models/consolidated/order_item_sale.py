from datetime import datetime
from sqlalchemy import String, Integer, Boolean, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class OrderItemSale(ConsolidatedBase):
    __tablename__ = 'order_item_sale'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    order_header_id: Mapped[str] = mapped_column(String(255), ForeignKey('order_header.id', name='fk_order_item_sale_order_header'))
    product_distributor_id: Mapped[str] = mapped_column(String(255))
    ean: Mapped[str | None] = mapped_column(String(50))
    product_id: Mapped[str | None] = mapped_column(String(255), ForeignKey('product.id', name='order_item_sale_fk'))
    promotion_header_id: Mapped[str] = mapped_column(String(255),
                                                     ForeignKey('promotion_header.id', name='fk_order_item_sale_promotion_header'))
    promotion_item_id: Mapped[str] = mapped_column(String(255))
    subsidized: Mapped[bool] = mapped_column(Boolean)
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    final_price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    sub_total: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    sub_total_with_taxes: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
