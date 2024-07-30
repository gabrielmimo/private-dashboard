from datetime import datetime
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class Client(ConsolidatedBase):
    __tablename__ = 'client'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    cnpj: Mapped[str] = mapped_column(String(50))
    razao_social: Mapped[str] = mapped_column(String(255))
    drugstore: Mapped[bool] = mapped_column(Boolean)
    state: Mapped[str] = mapped_column(String(2))
    city: Mapped[str] = mapped_column(String(255))
    zipcode: Mapped[str] = mapped_column(String(20))
    registration_date: Mapped[datetime | None] = mapped_column(DateTime)
    registration_distributor: Mapped[str | None] = mapped_column(String(255))
    recommended_by: Mapped[str | None] = mapped_column(String(255))
    first_login: Mapped[datetime | None] = mapped_column(DateTime)
    first_login_distributor: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
