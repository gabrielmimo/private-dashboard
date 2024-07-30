from datetime import datetime
from sqlalchemy import String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class SyncLog(ConsolidatedBase):
    __tablename__ = 'sync_log'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    description: Mapped[str] = mapped_column(String(255))
    execution_begin: Mapped[datetime] = mapped_column(DateTime)
    execution_end: Mapped[datetime | None] = mapped_column(DateTime)
    sync_exception: Mapped[str | None] = mapped_column(Text)
