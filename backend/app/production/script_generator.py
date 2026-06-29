def generate_script(topic: str, country: str, language: str) -> dict[str, object]:
    hook = "Esto parece pequeno, pero puede cambiar como una empresa crea contenido."
    script = (
        f"{hook} En {country}, muchas marcas pierden tiempo creando piezas sin estrategia. "
        f"La oportunidad de hoy es explicar {topic} con una historia breve, clara y útil. "
        "Primero mostramos el problema, luego una comparación simple y cerramos con una idea aplicable."
    )
    return {"hook": hook, "script": script, "language": language, "duration_seconds": 38}
