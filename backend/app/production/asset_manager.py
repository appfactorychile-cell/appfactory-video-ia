from app.models.production import Asset


def define_assets() -> list[Asset]:
    return [
        Asset("asset-1", "Escenario", "Centro de control de contenido IA en estilo SaaS oscuro.", "Definido"),
        Asset("asset-2", "Personaje", "Narrador profesional, cercano y confiable.", "Definido"),
        Asset("asset-3", "Gráficos", "Indicadores de oportunidad, ROI y calidad.", "Definido"),
        Asset("asset-4", "Plantilla", "Formato vertical 9:16 con subtítulos seguros.", "Definido"),
    ]

