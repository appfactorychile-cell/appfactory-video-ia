from datetime import datetime
from types import SimpleNamespace

from app.database.session import SessionLocal
from app.projects import document_parser, knowledge_loader, project_sources, source_validator
from app.repositories import DocumentRepository, ProjectRepository


def _project_to_domain(project):
    if project is None:
        return None
    return SimpleNamespace(
        id=project.id,
        name=project.name,
        description=project.description,
        primary_language=project.primary_language,
        country=project.country,
        project_type=project.project_type,
        status=project.status,
        created_at=project.created_at,
    )


def _document_to_domain(document):
    source_file = SimpleNamespace(
        id=document.id,
        filename=document.filename,
        file_type=document.file_type,
        size_bytes=document.size_bytes,
        status=document.status,
        uploaded_at=document.created_at,
    )
    return SimpleNamespace(
        id=document.id,
        project_id=document.project_id,
        source_file=source_file,
        authorized_for_ai=document.authorized_for_ai,
        parser_status=document.parser_status,
    )


def seed_projects() -> None:
    with SessionLocal() as db:
        repo = ProjectRepository(db)
        if repo.list():
            return
        repo.create(
            name="Codigo Nebula",
            description="Proyecto ficticio para validar modo proyecto sin procesar documentos reales.",
            primary_language="Espanol",
            country="Chile",
            project_type="Serie",
        )


def list_projects():
    seed_projects()
    with SessionLocal() as db:
        return [_project_to_domain(project) for project in ProjectRepository(db).list()]


def create_project(project):
    with SessionLocal() as db:
        created = ProjectRepository(db).create(
            name=project.name,
            description=project.description,
            primary_language=project.primary_language,
            country=project.country,
            project_type=project.project_type,
        )
        return _project_to_domain(created)


def get_project(project_id: str):
    seed_projects()
    with SessionLocal() as db:
        return _project_to_domain(ProjectRepository(db).get(project_id))


def delete_project(project_id: str) -> bool:
    with SessionLocal() as db:
        return ProjectRepository(db).delete(project_id)


def add_document(project_id: str, filename: str, file_type: str, size_bytes: int):
    with SessionLocal() as db:
        project_repo = ProjectRepository(db)
        if project_repo.get(project_id) is None:
            raise KeyError(project_id)
        normalized_type = source_validator.normalize_file_type(file_type)
        supported = source_validator.is_supported(file_type)
        parser_status = document_parser.register_document_only(filename, normalized_type)
        document = DocumentRepository(db).create(
            project_id=project_id,
            filename=filename,
            file_type=normalized_type,
            size_bytes=size_bytes,
            authorized_for_ai=supported,
            parser_status=parser_status,
        )
        return _document_to_domain(document)


def list_documents(project_id: str):
    with SessionLocal() as db:
        if ProjectRepository(db).get(project_id) is None:
            raise KeyError(project_id)
        return [_document_to_domain(document) for document in DocumentRepository(db).list_by_project(project_id)]


def list_sources(project_id: str):
    documents = list_documents(project_id)
    return [
        project_sources.create_source(project_id, document.source_file.filename, document.source_file.file_type)
        for document in documents
        if document.authorized_for_ai
    ]


def activate_project(project_id: str):
    with SessionLocal() as db:
        project = ProjectRepository(db).activate(project_id)
        if project is None:
            raise KeyError(project_id)
        return _project_to_domain(project)


def deactivate_project() -> None:
    with SessionLocal() as db:
        ProjectRepository(db).deactivate_all()


def get_active_project():
    seed_projects()
    with SessionLocal() as db:
        return _project_to_domain(ProjectRepository(db).active())
