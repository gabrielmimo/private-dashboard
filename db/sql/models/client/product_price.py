from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Numeric, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class ProductPrice(ClientBase):
    __tablename__ = 'product_price'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(255))
    price_group_id: Mapped[int] = mapped_column(Integer, ForeignKey('price_group.id', name='fk_product_price_price_group'))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id', name='fk_product_price_product'))
    sku: Mapped[str] = mapped_column(String(20))
    price: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    final_price: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    suggested_price: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    allow_credit_down: Mapped[bool] = mapped_column(Boolean)
    allow_credit_up: Mapped[bool] = mapped_column(Boolean)
    allow_negotiation_down: Mapped[bool] = mapped_column(Boolean)
    allow_negotiation_up: Mapped[bool] = mapped_column(Boolean)
    allow_promotions: Mapped[bool] = mapped_column(Boolean)
    discount: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    min_quantity: Mapped[int | None] = mapped_column(Integer)
    max_quantity: Mapped[int | None] = mapped_column(Integer)
    min_price: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    negotiation_min_price: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    negotiation_max_price: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    negotiation_min_margin: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    teams_kickback: Mapped[dict | None] = mapped_column(JSONB)
    margin_kickback_ranges: Mapped[dict | None] = mapped_column(JSONB)
    seller_kickback: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
