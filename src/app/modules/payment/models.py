from src.app.infrastructure.database.base import Base
from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Numeric,
    Enum as SQLAlchemyEnum,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from src.app.shared.enums import CurrencyEnum, PaymentStatusEnum
from datetime import datetime, timezone


class PaymentModel(Base):
    __tablename__ = "payment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    payment_reference: Mapped[str] = mapped_column(String, unique=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    receiver_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(
        Numeric(precision=12, scale=2), nullable=False
    )
    currency: Mapped[CurrencyEnum] = mapped_column(
        SQLAlchemyEnum(CurrencyEnum), nullable=False, default=CurrencyEnum.INR
    )
    status: Mapped[PaymentStatusEnum] = mapped_column(
        SQLAlchemyEnum(PaymentStatusEnum),
        nullable=False,
        default=PaymentStatusEnum.PENDING,
    )
    idempotency_key: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    failure_reason: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    processed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None, nullable=True
    )
