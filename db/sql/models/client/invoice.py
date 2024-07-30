from db.sql.models.client.client_base import ClientBase
from datetime import datetime, date
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Numeric, Boolean, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Invoice(ClientBase):
    __tablename__ = 'invoice'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(255))
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey('client.id', name='fk_invoice_client'))
    order_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('simple_order_header.id', name='fk_invoice_order_header'))
    branch_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('branch.id', name='fk_invoice_branch'))
    warehouse_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('warehouse.id', name='fk_invoice_warehouse'))
    order_external_id: Mapped[int | None] = mapped_column(Integer)
    cnpj: Mapped[str] = mapped_column(String(20))
    our_number: Mapped[str | None] = mapped_column(String(255))
    emission_date: Mapped[date | None] = mapped_column(Date)
    due_date: Mapped[date | None] = mapped_column(Date)
    payment_date: Mapped[date | None] = mapped_column(Date)
    linha_digitavel: Mapped[str | None] = mapped_column(String(255))
    instalment: Mapped[int | None] = mapped_column(Integer)
    instalments: Mapped[int | None] = mapped_column(Integer)
    nfe_number: Mapped[str | None] = mapped_column(String(50))
    nfe_key: Mapped[str | None] = mapped_column(String(50))
    value: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    origin: Mapped[str | None] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(50))
    files: Mapped[dict | None] = mapped_column(JSONB)
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
