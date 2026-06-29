def make_executive_decision(opportunity_score: int, roi_percentage: float, risk_level: int) -> dict[str, object]:
    if opportunity_score >= 82 and roi_percentage >= 0 and risk_level <= 45:
        decision = "PRODUCIR"
        rationale = "La oportunidad combina demanda alta, riesgo controlado y retorno esperado positivo."
    elif opportunity_score >= 70 and risk_level <= 55:
        decision = "POSPONER"
        rationale = "Existe potencial, pero conviene esperar una ventana de costo o competencia mas favorable."
    elif risk_level > 65:
        decision = "NO PRODUCIR"
        rationale = "El riesgo editorial o de calidad supera el retorno esperado."
    else:
        decision = "VOLVER A ANALIZAR"
        rationale = "La senal aun no es suficiente para invertir recursos de produccion."
    return {
        "decision": decision,
        "rationale": rationale,
        "approved": decision == "PRODUCIR",
        "next_action": "Continuar con Content Brain" if decision == "PRODUCIR" else "No generar contenido todavia",
    }

