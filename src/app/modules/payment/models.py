from src.app.infrastructure.database.base import Base
from sqlalchemy import Integer, String, ForeignKey, Numeric, Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from src.app.shared.enums import CurrencyEnum


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
