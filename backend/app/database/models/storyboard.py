from sqlalchemy import ForeignKey, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampStatusMixin


class StoryboardORM(TimestampStatusMixin, Base):
    __tablename__ = "storyboards"

    idea_id: Mapped[str | None] = mapped_column(String(36), ForeignKey("ideas.id", ondelete="SET NULL"), nullable=True)
    title: Mapped[str] = mapped_column(String(240), nullable=False)
    hook: Mapped[str] = mapped_column(Text, default="", nullable=False)
    scenes: Mapped[list[dict]] = mapped_column(JSON, default=list, nullable=False)
