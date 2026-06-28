from app.models.project import KnowledgeSource


def create_source(project_id: str, filename: str, file_type: str) -> KnowledgeSource:
    return KnowledgeSource(
        project_id=project_id,
        source_type=file_type,
        name=filename,
        status="Registrada",
        authorized_scope="Disponible solo para este proyecto cuando este activo",
    )
