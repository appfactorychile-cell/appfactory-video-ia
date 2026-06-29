from app.models.production import Scene


def build_scenes() -> list[Scene]:
    return [
        Scene("scene-1", "Hook visual", "Texto cinético premium sobre fondo operativo oscuro.", 6, "Push-in lento"),
        Scene("scene-2", "Problema", "Creador revisando ideas dispersas antes de producir.", 10, "Plano medio con cortes rápidos"),
        Scene("scene-3", "Solución", "Pipeline IA ordenando guion, escenas y calidad.", 14, "Travelling lateral suave"),
        Scene("scene-4", "Cierre", "Resumen limpio con CTA responsable.", 8, "Plano fijo con subtítulos destacados"),
    ]

