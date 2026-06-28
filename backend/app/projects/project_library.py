from app.models.project import Project, ProjectDocument, SourceFile
from app.projects import document_parser, project_sources, source_validator

_projects: dict[str, Project] = {}
_documents: dict[str, list[ProjectDocument]] = {}
_sources = {}
_active_project_id: str | None = None


def seed_projects() -> None:
    if _projects:
        return
    project = Project(
        name="Codigo Nebula",
        description="Proyecto ficticio para validar modo proyecto sin procesar documentos reales.",
        primary_language="Espanol",
        country="Chile",
        project_type="Serie",
    )
    _projects[project.id] = project
    _documents[project.id] = []
    _sources[project.id] = []


def list_projects() -> list[Project]:
    seed_projects()
    return list(_projects.values())


def create_project(project: Project) -> Project:
    _projects[project.id] = project
    _documents[project.id] = []
    _sources[project.id] = []
    return project


def get_project(project_id: str) -> Project | None:
    seed_projects()
    return _projects.get(project_id)


def delete_project(project_id: str) -> bool:
    global _active_project_id
    if project_id not in _projects:
        return False
    del _projects[project_id]
    _documents.pop(project_id, None)
    _sources.pop(project_id, None)
    if _active_project_id == project_id:
        _active_project_id = None
    return True


def add_document(project_id: str, filename: str, file_type: str, size_bytes: int) -> ProjectDocument:
    if project_id not in _projects:
        raise KeyError(project_id)
    normalized_type = source_validator.normalize_file_type(file_type)
    status = "Registrado" if source_validator.is_supported(file_type) else "Tipo no soportado"
    parser_status = document_parser.register_document_only(filename, normalized_type)
    doc = ProjectDocument(
        project_id=project_id,
        source_file=SourceFile(filename=filename, file_type=normalized_type, size_bytes=size_bytes, status=status),
        authorized_for_ai=status == "Registrado",
        parser_status=parser_status,
    )
    _documents.setdefault(project_id, []).append(doc)
    if status == "Registrado":
        _sources.setdefault(project_id, []).append(project_sources.create_source(project_id, filename, normalized_type))
    return doc


def list_documents(project_id: str) -> list[ProjectDocument]:
    if project_id not in _projects:
        raise KeyError(project_id)
    return _documents.get(project_id, [])


def list_sources(project_id: str):
    if project_id not in _projects:
        raise KeyError(project_id)
    return _sources.get(project_id, [])


def activate_project(project_id: str) -> Project:
    global _active_project_id
    project = get_project(project_id)
    if project is None:
        raise KeyError(project_id)
    _active_project_id = project_id
    return project


def deactivate_project() -> None:
    global _active_project_id
    _active_project_id = None


def get_active_project() -> Project | None:
    seed_projects()
    if _active_project_id is None:
        return None
    return _projects.get(_active_project_id)
