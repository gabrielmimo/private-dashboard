from datetime import datetime
from sqlalchemy import String, Integer, Boolean, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class PromotionItem(ConsolidatedBase):
    __tablename__ = 'promotion_item'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    promotion_header_id: Mapped[str] = mapped_column(String(255),
                                                     ForeignKey('promotion_header.id', name='fk_promotion_item_promotion_header'))
    product_distributor_id: Mapped[str] = mapped_column(String(255))
    product_id: Mapped[str | None] = mapped_column(String(255), ForeignKey('product.id', name='promotion_item_fk'))
    item_quantity: Mapped[int | None] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    final_price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2, asdecimal=False))
    subsidized: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
