from app.models.project import ProjectMemory


def build_project_memory(project_id: str, project_name: str) -> ProjectMemory:
    return ProjectMemory(
        project_id=project_id,
        mode="Proyecto vinculado",
        summary=f"Memoria mock autorizada para {project_name}. No contiene documentos procesados todavia.",
        principles=[
            "Usar solo informacion autorizada por el usuario.",
            "No inventar datos internos del proyecto.",
            "Mantener el modo global disponible en todo momento.",
        ],
    )
