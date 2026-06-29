from app.models.production import RenderJob


def prepare_render() -> RenderJob:
    return RenderJob(format="Vertical 9:16", resolution="1080x1920", progress=100, status="Render mock listo")

