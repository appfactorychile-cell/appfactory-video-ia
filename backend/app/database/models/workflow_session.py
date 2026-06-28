from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampStatusMixin


class WorkflowSessionORM(TimestampStatusMixin, Base):
    __tablename__ = "workflow_sessions"

    channel_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    current_step: Mapped[str] = mapped_column(String(120), default="created", nullable=False)
    data: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
