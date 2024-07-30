from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Boolean, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Warehouse(ClientBase):
    __tablename__ = 'warehouse'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str | None] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    uf: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(50))
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
