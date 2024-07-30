from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class ClientDistributor(ConsolidatedBase):
    __tablename__ = 'client_distributor'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    distributor_id: Mapped[str] = mapped_column(String(255), ForeignKey('distributor.id', name='fk_client_distributor_distributor'))
    client_id: Mapped[str] = mapped_column(String(255), ForeignKey('client.id', name='fk_client_distributor_client'))
    name: Mapped[str] = mapped_column(String(255))
    registration_status: Mapped[str] = mapped_column(String(50))
    nexon_status: Mapped[str] = mapped_column(String(50))
    email: Mapped[str | None] = mapped_column(String(100))
    phone: Mapped[str | None] = mapped_column(String(100))
    first_login: Mapped[datetime | None] = mapped_column(DateTime)
    registration_date: Mapped[datetime | None] = mapped_column(DateTime)
    registration_distributor: Mapped[str | None] = mapped_column(String(255))
    recommended_by: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
