from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Boolean, Integer, DateTime, Text, ForeignKey  # ,Numeric
from sqlalchemy.orm import Mapped, mapped_column


class SimpleOrderHeader(ClientBase):
    __tablename__ = 'simple_order_header'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(255))
    branch_id: Mapped[int] = mapped_column(Integer, ForeignKey('branch.id', name='fk_simple_order_branch'))
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey('client.id', name='fk_simple_order_client'))
    price_group_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('price_group.id', name='fk_order_header_price_group'))
    warehouse_id: Mapped[int] = mapped_column(Integer, ForeignKey('warehouse.id', name='fk_simple_order_warehouse'))
    main_seller_id: Mapped[int] = mapped_column(Integer, ForeignKey('seller.id', name='fk_simple_order_main_seller'))
    seller_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('seller.id', name='fk_order_header_seller'))
    selected_seller_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('seller.id', name='fk_simple_order_seller'))
    user_role: Mapped[str | None] = mapped_column(String(50))
    origin: Mapped[str] = mapped_column(String(50))
    processed: Mapped[bool | None] = mapped_column(Boolean)
    status: Mapped[str | None] = mapped_column(String(50))
    order_date: Mapped[datetime] = mapped_column(DateTime)
    # original_order_total: Mapped[float] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    # original_order_total_with_taxes: Mapped[float] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    # total: Mapped[float] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    # total_with_taxes: Mapped[float] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    summary: Mapped[dict | None] = mapped_column(JSONB)
    status_label: Mapped[str | None] = mapped_column(String(255))
    status_reason: Mapped[str | None] = mapped_column(Text)
    payment: Mapped[dict] = mapped_column(JSONB)
    payment_status: Mapped[str | None] = mapped_column(String(50))
    status_log_history: Mapped[dict | None] = mapped_column(JSONB)
    files: Mapped[dict | None] = mapped_column(JSONB)
    erp_sync_status: Mapped[str | None] = mapped_column(String(100))
    external_ref: Mapped[dict | None] = mapped_column(JSONB)
    billing_date: Mapped[datetime] = mapped_column(DateTime)
    imported_date: Mapped[datetime | None] = mapped_column(DateTime)
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
