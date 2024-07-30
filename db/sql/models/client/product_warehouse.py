from db.sql.models.client.client_base import ClientBase
from datetime import datetime, date
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Boolean, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class ProductWarehouse(ClientBase):
    __tablename__ = 'product_warehouse'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(255))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id', name='fk_product_warehouse_product'))
    warehouse_id: Mapped[int] = mapped_column(Integer, ForeignKey('warehouse.id', name='fk_product_warehouse_warehouse'))
    sku: Mapped[str] = mapped_column(String(20))
    quantity_available: Mapped[int] = mapped_column(Integer)
    valid_until: Mapped[date | None] = mapped_column(Date)
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
