from app.models.animation import AnimationAsset


ASSET_CATEGORIES = {
    "Fondos": ["Ciudad nocturna", "Oficina moderna", "Mapa global", "Aula digital"],
    "Personajes": ["Narrador experto", "Emprendedora", "Analista", "Cliente curioso"],
    "Iconos": ["Cerebro IA", "Reloj", "Grafico", "Escudo"],
    "Objetos": ["Laptop", "Celular", "Documento", "Servidor"],
    "Elementos UI": ["Tarjeta KPI", "Panel de alerta", "Boton", "Barra de progreso"],
    "Graficos": ["Barras", "Linea de crecimiento", "ROI", "Comparacion"],
    "Mapas": ["Mapa mundial", "Pais destacado", "Ruta global", "Zona horaria"],
    "Flechas": ["Flecha curva", "Flecha directa", "Conector", "Pulso"],
    "Textos": ["Titulo grande", "Dato clave", "CTA", "Etiqueta"],
}


def list_assets() -> list[AnimationAsset]:
    assets: list[AnimationAsset] = []
    for category, names in ASSET_CATEGORIES.items():
        for index, name in enumerate(names, start=1):
            asset_id = f"{category.lower().replace(' ', '-')}-{index}"
            assets.append(AnimationAsset(asset_id, category, name, "Vector premium", f"Asset mock preparado para videos animados: {name}."))
    return assets


def grouped_assets() -> dict[str, list[AnimationAsset]]:
    result: dict[str, list[AnimationAsset]] = {}
    for asset in list_assets():
        result.setdefault(asset.category, []).append(asset)
    return result


def select_assets_for_video(video_type: str) -> list[AnimationAsset]:
    assets = list_assets()
    preferred = ["Fondos", "Personajes", "Iconos", "Elementos UI", "Textos"]
    if video_type in {"Infographic", "Business"}:
        preferred.extend(["Graficos", "Mapas", "Flechas"])
    return [asset for asset in assets if asset.category in preferred][:12]
