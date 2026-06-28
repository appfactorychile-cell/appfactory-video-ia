from sqlalchemy import Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampStatusMixin


class ChannelORM(TimestampStatusMixin, Base):
    __tablename__ = "channels"

    name: Mapped[str] = mapped_column(String(180), nullable=False, index=True)
    target_country: Mapped[str] = mapped_column(String(120), nullable=False)
    language: Mapped[str] = mapped_column(String(80), nullable=False)
    timezone: Mapped[str] = mapped_column(String(120), nullable=False)
    niche: Mapped[str] = mapped_column(String(120), nullable=False)
    visual_style: Mapped[str] = mapped_column(String(180), nullable=False)
    ai_voice: Mapped[str] = mapped_column(String(180), nullable=False)
    daily_video_count: Mapped[int] = mapped_column(Integer, default=8, nullable=False)
    publishing_times: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    connected_platforms: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    content_rules: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
