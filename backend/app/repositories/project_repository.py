from sqlalchemy import select, update

from app.database.models.project import ProjectORM
from app.repositories.base_repository import BaseRepository


class ProjectRepository(BaseRepository):
    def list(self) -> list[ProjectORM]:
        return list(self.db.scalars(select(ProjectORM).order_by(ProjectORM.created_at.desc())))

    def get(self, project_id: str) -> ProjectORM | None:
        return self.db.get(ProjectORM, project_id)

    def create(self, name: str, description: str, primary_language: str, country: str, project_type: str) -> ProjectORM:
        project = ProjectORM(
            name=name,
            description=description,
            primary_language=primary_language,
            country=country,
            project_type=project_type,
            status="Disponible",
        )
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def delete(self, project_id: str) -> bool:
        project = self.get(project_id)
        if project is None:
            return False
        self.db.delete(project)
        self.db.commit()
        return True

    def activate(self, project_id: str) -> ProjectORM | None:
        project = self.get(project_id)
        if project is None:
            return None
        self.db.execute(update(ProjectORM).values(is_active=False))
        project.is_active = True
        project.status = "Activo"
        self.db.commit()
        self.db.refresh(project)
        return project

    def deactivate_all(self) -> None:
        self.db.execute(update(ProjectORM).values(is_active=False, status="Disponible"))
        self.db.commit()

    def active(self) -> ProjectORM | None:
        return self.db.scalar(select(ProjectORM).where(ProjectORM.is_active.is_(True)))
