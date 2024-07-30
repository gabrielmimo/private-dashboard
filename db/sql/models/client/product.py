from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Boolean, Integer, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Product(ClientBase):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    sku: Mapped[str] = mapped_column(String(20))
    ean: Mapped[str] = mapped_column(String(20))
    maker: Mapped[str] = mapped_column(String(255))
    category: Mapped[str] = mapped_column(String(255))
    principle: Mapped[str] = mapped_column(String(255))
    similar: Mapped[str] = mapped_column(String(255))
    reference: Mapped[str] = mapped_column(String(255))
    complementary_description: Mapped[str] = mapped_column(Text())
    box_quantity: Mapped[int] = mapped_column(Integer)
    available_nexon: Mapped[bool | None] = mapped_column(Boolean)
    available_nexoff: Mapped[bool | None] = mapped_column(Boolean)
    controlled: Mapped[bool | None] = mapped_column(Boolean)
    documentation_required: Mapped[bool | None] = mapped_column(Boolean)
    launch: Mapped[bool | None] = mapped_column(Boolean)
    partner_maker: Mapped[bool] = mapped_column(Boolean)
    active: Mapped[bool | None] = mapped_column(Boolean)
    custom_fields: Mapped[dict | None] = mapped_column(JSONB)
    extra_search: Mapped[dict | None] = mapped_column(JSONB)
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))

    # Relationships
    product_pmc_pf: Mapped[list['ProductPMCPF'] | None] = relationship(back_populates='product')
