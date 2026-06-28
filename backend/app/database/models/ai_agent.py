from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampStatusMixin


class AIAgentORM(TimestampStatusMixin, Base):
    __tablename__ = "ai_agents"

    name: Mapped[str] = mapped_column(String(180), nullable=False, unique=True)
    specialty: Mapped[str] = mapped_column(String(180), nullable=False)
    objective: Mapped[str] = mapped_column(Text, default="", nullable=False)
    confidence_level: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
