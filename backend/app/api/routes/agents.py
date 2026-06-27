from typing import Optional

from fastapi import APIRouter, HTTPException

from app.schemas.agent_schema import (
    AgentProfileSchema,
    AgentSimulationRequest,
    AgentSimulationResponse,
    AgentStatusOverviewResponse,
)
from app.services import agent_service

router = APIRouter(prefix="/agents", tags=["AI Agents Platform"])


@router.get("", response_model=list[AgentProfileSchema])
def list_agents() -> list[AgentProfileSchema]:
    return agent_service.list_agents()


@router.get("/status", response_model=AgentStatusOverviewResponse)
def get_agents_status() -> AgentStatusOverviewResponse:
    return agent_service.get_status()


@router.post("/simulate", response_model=AgentSimulationResponse)
def simulate_agents(payload: Optional[AgentSimulationRequest] = None) -> AgentSimulationResponse:
    return agent_service.simulate(payload or AgentSimulationRequest())


@router.get("/{agent_name}", response_model=AgentProfileSchema)
def get_agent(agent_name: str) -> AgentProfileSchema:
    try:
        return agent_service.get_agent(agent_name)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Agent not found") from exc


