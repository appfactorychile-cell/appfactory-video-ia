from dataclasses import asdict
from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from app.projects import project_library, project_manager
from app.schemas.project_schema import (
    ActiveProjectResponse,
    DocumentCreate,
    ProjectCreate,
    ProjectDetailResponse,
    ProjectDocumentSchema,
    ProjectMemorySchema,
    ProjectSchema,
    SourceFileSchema,
    SupportedSourcesResponse,
    SUPPORTED_DOCUMENT_TYPES,
)

router = APIRouter(prefix="/projects", tags=["Project Source Library"])


def _iso(value: datetime) -> str:
    return value.isoformat()


def _project_schema(project) -> ProjectSchema:
    data = asdict(project)
    data["created_at"] = _iso(project.created_at)
    return ProjectSchema(**data)


def _document_schema(document) -> ProjectDocumentSchema:
    source = asdict(document.source_file)
    source["uploaded_at"] = _iso(document.source_file.uploaded_at)
    return ProjectDocumentSchema(
        id=document.id,
        project_id=document.project_id,
        source_file=SourceFileSchema(**source),
        authorized_for_ai=document.authorized_for_ai,
        parser_status=document.parser_status,
    )


def _detail(project_id: str) -> ProjectDetailResponse:
    project = project_library.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    memory = project_manager.build_memory(project)
    return ProjectDetailResponse(
        project=_project_schema(project),
        documents=[_document_schema(item) for item in project_library.list_documents(project_id)],
        sources=[asdict(item) for item in project_library.list_sources(project_id)],
        memory=ProjectMemorySchema(
            project_id=memory.project_id,
            mode=memory.mode,
            summary=memory.summary,
            principles=memory.principles,
            updated_at=_iso(memory.updated_at),
        ),
    )


@router.get("", response_model=list[ProjectSchema])
def list_projects() -> list[ProjectSchema]:
    return [_project_schema(project) for project in project_library.list_projects()]


@router.post("", response_model=ProjectSchema, status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate) -> ProjectSchema:
    project = project_manager.create_project(
        name=payload.name,
        description=payload.description,
        primary_language=payload.primary_language,
        country=payload.country,
        project_type=payload.project_type,
    )
    return _project_schema(project)


@router.get("/active", response_model=ActiveProjectResponse)
def get_active_project() -> ActiveProjectResponse:
    project = project_library.get_active_project()
    if project is None:
        return ActiveProjectResponse(
            mode="Contenido global",
            active_project=None,
            message="La IA esta trabajando sin proyecto vinculado.",
        )
    return ActiveProjectResponse(
        mode="Proyecto vinculado",
        active_project=_project_schema(project),
        message=f"La IA usara solo informacion autorizada de {project.name}.",
    )


@router.post("/deactivate", response_model=ActiveProjectResponse)
def deactivate_project() -> ActiveProjectResponse:
    project_library.deactivate_project()
    return ActiveProjectResponse(
        mode="Contenido global",
        active_project=None,
        message="Modo global activado. La IA no usara informacion de proyectos.",
    )


@router.get("/supported-sources", response_model=SupportedSourcesResponse)
def supported_sources() -> SupportedSourcesResponse:
    return SupportedSourcesResponse(
        supported_document_types=SUPPORTED_DOCUMENT_TYPES,
        note="Arquitectura preparada para registrar fuentes. El procesamiento real queda para fases futuras.",
    )


@router.get("/{project_id}", response_model=ProjectDetailResponse)
def get_project(project_id: str) -> ProjectDetailResponse:
    return _detail(project_id)


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: str) -> None:
    if not project_library.delete_project(project_id):
        raise HTTPException(status_code=404, detail="Project not found")


@router.post("/{project_id}/documents", response_model=ProjectDocumentSchema, status_code=status.HTTP_201_CREATED)
def add_document(project_id: str, payload: DocumentCreate) -> ProjectDocumentSchema:
    try:
        document = project_library.add_document(project_id, payload.filename, payload.file_type, payload.size_bytes)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Project not found") from exc
    return _document_schema(document)


@router.get("/{project_id}/documents", response_model=list[ProjectDocumentSchema])
def list_documents(project_id: str) -> list[ProjectDocumentSchema]:
    try:
        return [_document_schema(item) for item in project_library.list_documents(project_id)]
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Project not found") from exc


@router.post("/{project_id}/activate", response_model=ActiveProjectResponse)
def activate_project(project_id: str) -> ActiveProjectResponse:
    try:
        project = project_library.activate_project(project_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Project not found") from exc
    return ActiveProjectResponse(
        mode="Proyecto vinculado",
        active_project=_project_schema(project),
        message=f"Proyecto activo: {project.name}. La IA solo usara fuentes autorizadas de este proyecto.",
    )
