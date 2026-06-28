from app.models.project import Project
from app.projects import knowledge_loader, project_library


def create_project(name: str, description: str, primary_language: str, country: str, project_type: str) -> Project:
    return project_library.create_project(
        Project(
            name=name,
            description=description,
            primary_language=primary_language,
            country=country,
            project_type=project_type,
        )
    )


def build_memory(project: Project):
    return knowledge_loader.build_project_memory(project.id, project.name)


def active_mode_label() -> str:
    return "Proyecto vinculado" if project_library.get_active_project() else "Contenido global"
