from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampStatusMixin


class SettingORM(TimestampStatusMixin, Base):
    __tablename__ = "settings"

    key: Mapped[str] = mapped_column(String(180), nullable=False, unique=True)
    value: Mapped[str] = mapped_column(Text, default="", nullable=False)
    scope: Mapped[str] = mapped_column(String(80), default="global", nullable=False)
