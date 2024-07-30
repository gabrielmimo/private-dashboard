from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Numeric, Boolean, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Client(ClientBase):
    __tablename__ = 'client'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str] = mapped_column(String(20))
    name: Mapped[str] = mapped_column(String(255))
    cnpj: Mapped[str] = mapped_column(String(20))
    razao_social: Mapped[str] = mapped_column(String(255))
    cnpj_matriz: Mapped[str | None] = mapped_column(String(20))
    email_erp: Mapped[str | None] = mapped_column(String(255))
    phone: Mapped[str | None] = mapped_column(String(20))
    cep: Mapped[str | None] = mapped_column(String(20))
    city: Mapped[str | None] = mapped_column(String(255))
    state: Mapped[str] = mapped_column(String(2))
    address: Mapped[str | None] = mapped_column(String(255))
    credit_limit: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    credit_status: Mapped[str | None] = mapped_column(String(50))
    documentation_status: Mapped[str | None] = mapped_column(String(50))
    drugstore: Mapped[bool | None] = mapped_column(Boolean)
    tax_free: Mapped[bool] = mapped_column(Boolean)
    client_tax_code: Mapped[str | None] = mapped_column(String(255))
    client_margin_code: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(50))
    custom_fields: Mapped[dict | None] = mapped_column(JSONB)
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
