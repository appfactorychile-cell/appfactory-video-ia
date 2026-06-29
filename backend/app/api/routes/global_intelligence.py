from fastapi import APIRouter

from app.intelligence import budget_optimizer, global_intelligence
from app.schemas.global_intelligence_schema import (
    BudgetOptimizationRequest,
    BudgetOptimizationResponse,
    ExecutiveDashboardResponse,
    GlobalOpportunityRequest,
    GlobalOpportunityResponse,
)

router = APIRouter(prefix="/global-intelligence", tags=["Global Opportunity Intelligence"])


@router.post("/audit", response_model=GlobalOpportunityResponse, summary="Auditoria Mundial")
def audit_global_opportunity(payload: GlobalOpportunityRequest) -> GlobalOpportunityResponse:
    return global_intelligence.analyze_global_opportunity(
        topic=payload.topic,
        country=payload.country,
        language=payload.language,
        niche=payload.niche,
        daily_budget_usd=payload.daily_budget_usd,
    )


@router.post("/executive-decision", response_model=GlobalOpportunityResponse, summary="Director Ejecutivo IA")
def executive_decision(payload: GlobalOpportunityRequest) -> GlobalOpportunityResponse:
    return audit_global_opportunity(payload)


@router.get("/executive-dashboard", response_model=ExecutiveDashboardResponse, summary="Executive Dashboard")
def executive_dashboard() -> ExecutiveDashboardResponse:
    return global_intelligence.executive_dashboard()


@router.post("/budget/optimize", response_model=BudgetOptimizationResponse, summary="Budget Manager")
def optimize_budget(payload: BudgetOptimizationRequest) -> BudgetOptimizationResponse:
    candidates = payload.candidates or [
        {"title": "IA practica para pymes", "opportunity_score": 93, "estimated_cost_usd": 5.95, "expected_roi_percentage": 210},
        {"title": "Ahorro energetico local", "opportunity_score": 88, "estimated_cost_usd": 4.4, "expected_roi_percentage": 174},
        {"title": "Historia curiosa de tecnologia", "opportunity_score": 77, "estimated_cost_usd": 6.2, "expected_roi_percentage": 96},
        {"title": "Tendencia saturada de productividad", "opportunity_score": 61, "estimated_cost_usd": 5.1, "expected_roi_percentage": 24},
    ]
    return budget_optimizer.optimize_budget(payload.daily_budget_usd, candidates)

