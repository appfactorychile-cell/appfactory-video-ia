from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampStatusMixin


class DocumentORM(TimestampStatusMixin, Base):
    __tablename__ = "documents"

    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("projects.id", ondelete="CASCADE"), index=True, nullable=False)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_type: Mapped[str] = mapped_column(String(60), nullable=False)
    size_bytes: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    authorized_for_ai: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    parser_status: Mapped[str] = mapped_column(Text, default="Registrado, no procesado", nullable=False)
