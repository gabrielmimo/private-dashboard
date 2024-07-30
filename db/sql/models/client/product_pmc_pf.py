from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Integer, String, Boolean, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ProductPMCPF(ClientBase):
    __tablename__ = 'product_pmc_pf'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(255))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id', name='fk_pmc_pf_product'))
    sku: Mapped[str] = mapped_column(String(20))
    uf: Mapped[str] = mapped_column(String(2))
    industry_price: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    pmc: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime | None] = mapped_column(DateTime)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))

    # Relationships
    product: Mapped['Product'] = relationship(back_populates='product_pmc_pf')
