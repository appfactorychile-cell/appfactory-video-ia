from sqlalchemy import ForeignKey, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampStatusMixin


class ProductionPlanORM(TimestampStatusMixin, Base):
    __tablename__ = "production_plans"

    storyboard_id: Mapped[str | None] = mapped_column(String(36), ForeignKey("storyboards.id", ondelete="SET NULL"), nullable=True)
    narrator: Mapped[str] = mapped_column(String(180), default="", nullable=False)
    visual_style: Mapped[str] = mapped_column(String(180), default="", nullable=False)
    format: Mapped[str] = mapped_column(String(80), default="Vertical 9:16", nullable=False)
    platforms: Mapped[list[str]] = mapped_column(JSON, default=list, nullable=False)
    settings: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
