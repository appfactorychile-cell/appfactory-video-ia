from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class SourceFile:
    filename: str
    file_type: str
    size_bytes: int
    status: str
    uploaded_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass(slots=True)
class ProjectDocument:
    project_id: str
    source_file: SourceFile
    authorized_for_ai: bool = True
    parser_status: str = "Registrado, no procesado"
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass(slots=True)
class KnowledgeSource:
    project_id: str
    source_type: str
    name: str
    status: str
    authorized_scope: str
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass(slots=True)
class ProjectMemory:
    project_id: str
    mode: str
    summary: str
    principles: list[str]
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class Project:
    name: str
    description: str
    primary_language: str
    country: str
    project_type: str
    status: str = "Disponible"
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
