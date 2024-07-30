from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.sql.models.consolidated.consolidated_base import ConsolidatedBase


class BranchDistributor(ConsolidatedBase):
    __tablename__ = 'branch_distributor'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    branch_id: Mapped[str] = mapped_column(String(255))
    distributor_id: Mapped[str] = mapped_column(String(255), ForeignKey('distributor.id', name='fk_branch_distributor_distributor'))
    external_id: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    type: Mapped[str] = mapped_column(String(255))
    main: Mapped[bool] = mapped_column(Boolean)
    complementary: Mapped[bool] = mapped_column(Boolean)
    taxes_calculation_mode: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    imported_at: Mapped[datetime] = mapped_column(DateTime)
