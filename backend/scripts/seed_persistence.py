from app.database.init_db import init_database
from app.database.session import SessionLocal
from app.repositories import ChannelRepository, DocumentRepository, ProjectRepository, UserRepository


def run() -> None:
    init_database()
    with SessionLocal() as db:
        users = UserRepository(db)
        projects = ProjectRepository(db)
        channels = ChannelRepository(db)
        documents = DocumentRepository(db)

        if users.get_by_email("owner@appfactorychile.local") is None:
            users.create("owner@appfactorychile.local", "AppFactoryChile Owner", "owner")

        existing_projects = projects.list()
        while len(existing_projects) < 2:
            projects.create(
                name=f"Proyecto Persistente {len(existing_projects) + 1}",
                description="Proyecto creado para validar persistencia PostgreSQL.",
                primary_language="Espanol",
                country="Chile",
                project_type="Cliente",
            )
            existing_projects = projects.list()

        existing_channels = channels.list()
        while len(existing_channels) < 3:
            index = len(existing_channels) + 1
            channels.create(
                name=f"Canal Persistente {index}",
                target_country="Chile",
                language="Espanol",
                timezone="America/Santiago",
                niche="Tecnologia",
                visual_style="Premium oscuro",
                ai_voice="Narrador natural",
                daily_video_count=8,
                publishing_times=["08:00", "13:00", "17:00", "21:00"],
                connected_platforms=["YouTube Shorts"],
                content_rules=["Contenido original", "Sin derechos de autor ajenos"],
            )
            existing_channels = channels.list()

        first_project = projects.list()[0]
        existing_documents = documents.list_by_project(first_project.id)
        sample_docs = [
            ("brief.pdf", "PDF", 245000),
            ("tono.md", "Markdown", 32000),
            ("datos.csv", "CSV", 88000),
            ("estructura.json", "JSON", 12000),
            ("referencia.txt", "TXT", 9000),
        ]
        for filename, file_type, size in sample_docs[len(existing_documents):5]:
            documents.create(
                project_id=first_project.id,
                filename=filename,
                file_type=file_type,
                size_bytes=size,
                authorized_for_ai=True,
                parser_status=f"{filename} registrado. Procesamiento real pendiente.",
            )

        print("Persistence seed complete")
        print(f"users: 1")
        print(f"projects: {len(projects.list())}")
        print(f"channels: {len(channels.list())}")
        print(f"documents in first project: {len(documents.list_by_project(first_project.id))}")


if __name__ == "__main__":
    run()
