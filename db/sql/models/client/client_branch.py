from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Numeric, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class ClientBranch(ClientBase):
    __tablename__ = 'client_branch'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(255))
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey('client.id', name='fk_client_branch_client'))
    branch_id: Mapped[int] = mapped_column(Integer, ForeignKey('branch.id', name='fk_client_branch_branch'))
    warehouse_id: Mapped[int] = mapped_column(Integer, ForeignKey('warehouse.id', name='fk_client_branch_warehouse'))
    price_group_id: Mapped[int] = mapped_column(Integer, ForeignKey('price_group.id', name='fk_client_branch_price_group'))
    seller_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('seller.id', name='fk_client_branch_seller'))
    main_seller: Mapped[bool | None] = mapped_column(Boolean)
    module: Mapped[str] = mapped_column(String(50))
    cnpj: Mapped[str] = mapped_column(String(20))
    payment_conditions: Mapped[dict | None] = mapped_column(JSONB)
    order_min_value: Mapped[float] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    medium_term: Mapped[int | None] = mapped_column(Integer)
    sellers_selector: Mapped[dict | None] = mapped_column(JSONB)
    tax_free: Mapped[bool] = mapped_column(Boolean)
    client_tax_code: Mapped[str | None] = mapped_column(String(255))
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
