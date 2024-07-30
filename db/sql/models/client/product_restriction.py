from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class ProductRestriction(ClientBase):
    __tablename__ = 'product_restriction'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(255))
    branch_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('branch.id', name='fk_product_restriction_branch'))
    warehouse_id: Mapped[str | None] = mapped_column(String(255))
    module: Mapped[str | None] = mapped_column(String(50))
    client_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('client.id', name='fk_product_restriction_client'))
    client_cnpj: Mapped[str | None] = mapped_column(String(20))
    client_uf: Mapped[str | None] = mapped_column(String(2))
    product_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('product.id', name='fk_product_restriction_product'))
    product_sku: Mapped[str | None] = mapped_column(String(20))
    product_maker: Mapped[str | None] = mapped_column(String(255))
    product_category: Mapped[str | None] = mapped_column(String(255))
    product_principle: Mapped[str | None] = mapped_column(String(255))
    seller_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('seller.id', name='fk_product_restriction_seller'))
    supervisor_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('seller.id', name='fk_product_restriction_supervisor'))
    max_quantity: Mapped[int | None] = mapped_column(Integer)
    periodicity: Mapped[str | None] = mapped_column(String(50))
    client_extra_params: Mapped[dict | None] = mapped_column(JSONB)
    product_extra_params: Mapped[dict | None] = mapped_column(JSONB)
    seller_extra_params: Mapped[dict | None] = mapped_column(JSONB)
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
