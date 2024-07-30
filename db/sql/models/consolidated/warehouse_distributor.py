from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class WarehouseDistributor(ConsolidatedBase):
    __tablename__ = 'warehouse_distributor'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    warehouse_id: Mapped[str] = mapped_column(String(255))
    distributor_id: Mapped[str] = mapped_column(String(255), ForeignKey('distributor.id', name='fk_warehouse_distributor_distributor'))
    external_id: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    uf: Mapped[str] = mapped_column(String(2))
    status: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
