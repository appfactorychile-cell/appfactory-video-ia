from sqlalchemy import select

from app.database.models.document import DocumentORM
from app.repositories.base_repository import BaseRepository


class DocumentRepository(BaseRepository):
    def list_by_project(self, project_id: str) -> list[DocumentORM]:
        return list(self.db.scalars(select(DocumentORM).where(DocumentORM.project_id == project_id).order_by(DocumentORM.created_at.desc())))

    def create(self, project_id: str, filename: str, file_type: str, size_bytes: int, authorized_for_ai: bool, parser_status: str) -> DocumentORM:
        document = DocumentORM(
            project_id=project_id,
            filename=filename,
            file_type=file_type,
            size_bytes=size_bytes,
            authorized_for_ai=authorized_for_ai,
            parser_status=parser_status,
            status="Registrado" if authorized_for_ai else "Tipo no soportado",
        )
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document
