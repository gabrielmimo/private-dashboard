from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Numeric, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class SimpleOrderItem(ClientBase):
    __tablename__ = 'simple_order_item'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey('simple_order_header.id', name='fk_simple_order_item_simple_order'))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id', name='fk_simple_order_item_product'))
    price_group_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('price_group.id', name='fk_order_item_price_group'))
    selected_seller_id: Mapped[int | None] = mapped_column(Integer)
    external_id: Mapped[str | None] = mapped_column(String(255))
    status_label: Mapped[str | None] = mapped_column(String(255))
    quantity_requested: Mapped[int] = mapped_column(Integer)
    quantity_attended: Mapped[int | None] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    final_price: Mapped[float] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    # sub_total: Mapped[float] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    # sub_total_with_taxes: Mapped[float] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    subsidized: Mapped[bool] = mapped_column(Boolean)
    returned: Mapped[bool] = mapped_column(Boolean)
    returned_date: Mapped[datetime | None] = mapped_column(DateTime)
    returned_quantity: Mapped[int | None] = mapped_column(Integer)
    returned_reason: Mapped[str | None] = mapped_column(String(255))
    summary: Mapped[dict | None] = mapped_column(JSONB)
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
