from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class ClientResponsible(ConsolidatedBase):
    __tablename__ = 'client_responsible'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    client_id: Mapped[str] = mapped_column(String(255), ForeignKey('client.id', name='fk_client_responsible_client'))
    user_id: Mapped[str] = mapped_column(String(255), ForeignKey('user.id', name='fk_client_responsible_user'))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
