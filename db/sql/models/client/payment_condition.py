from db.sql.models.client.client_base import ClientBase
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Numeric, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class PaymentCondition(ClientBase):
    __tablename__ = 'payment_condition'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    external_id: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    branch_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('branch.id', name='fk_payment_condition_branch'))
    price_group_id: Mapped[int | None] = mapped_column(Integer, ForeignKey('price_group.id', name='fk_payment_condition_price_group'))
    method: Mapped[str] = mapped_column(String(50))
    medium_term: Mapped[int | None] = mapped_column(Integer)
    instalments: Mapped[int | None] = mapped_column(Integer)
    times_in_days: Mapped[dict | None] = mapped_column(JSONB)
    discount: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    order_min_value: Mapped[float | None] = mapped_column(Numeric(precision=12, scale=4, asdecimal=False))
    extra_params: Mapped[dict | None] = mapped_column(JSONB)
    sync_status: Mapped[str] = mapped_column(String(100))
    removed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hash_erp: Mapped[str | None] = mapped_column(String(255))
    hash_code: Mapped[int] = mapped_column(Integer)
    datasource_id: Mapped[str | None] = mapped_column(String(50))
