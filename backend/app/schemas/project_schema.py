from pydantic import BaseModel, Field


SUPPORTED_DOCUMENT_TYPES = ["PDF", "DOCX", "TXT", "Markdown", "CSV", "JSON", "HTML", "PNG", "JPG", "WEBP", "MP4", "MP3"]
PROJECT_TYPES = ["Empresa", "Marca", "Libro", "Novela", "Serie", "Curso", "Producto", "Cliente", "Canal", "Otro"]


class ProjectCreate(BaseModel):
    name: str = Field(..., examples=["Codigo Nebula"])
    description: str = Field(..., examples=["Universo narrativo para videos de ciencia ficcion responsable"])
    primary_language: str = Field(..., examples=["Espanol"])
    country: str = Field(..., examples=["Chile"])
    project_type: str = Field(..., examples=["Serie"])


class ProjectSchema(ProjectCreate):
    id: str
    status: str
    created_at: str


class DocumentCreate(BaseModel):
    filename: str = Field(..., examples=["biblia-del-proyecto.pdf"])
    file_type: str = Field(..., examples=["PDF"])
    size_bytes: int = Field(default=0, ge=0)


class SourceFileSchema(BaseModel):
    id: str
    filename: str
    file_type: str
    size_bytes: int
    status: str
    uploaded_at: str


class ProjectDocumentSchema(BaseModel):
    id: str
    project_id: str
    source_file: SourceFileSchema
    authorized_for_ai: bool
    parser_status: str


class KnowledgeSourceSchema(BaseModel):
    id: str
    project_id: str
    source_type: str
    name: str
    status: str
    authorized_scope: str


class ProjectMemorySchema(BaseModel):
    project_id: str
    mode: str
    summary: str
    principles: list[str]
    updated_at: str


class ActiveProjectResponse(BaseModel):
    mode: str
    active_project: ProjectSchema | None
    message: str


class ProjectDetailResponse(BaseModel):
    project: ProjectSchema
    documents: list[ProjectDocumentSchema]
    sources: list[KnowledgeSourceSchema]
    memory: ProjectMemorySchema


class SupportedSourcesResponse(BaseModel):
    supported_document_types: list[str]
    note: str
