from fastapi import APIRouter

from app.schemas.workflow_schema import (
    WorkflowChannelCreate,
    WorkflowChooseHookRequest,
    WorkflowChooseIdeaRequest,
    WorkflowCreateChannelResponse,
    WorkflowHooksResponse,
    WorkflowIdeasResponse,
    WorkflowOpportunityResponse,
    WorkflowProductionPlanResponse,
    WorkflowReadyResponse,
    WorkflowSelectedHookResponse,
    WorkflowSelectedIdeaResponse,
    WorkflowStateResponse,
    WorkflowStepRequest,
    WorkflowStoryResponse,
)
from app.services import workflow_service

router = APIRouter(prefix="/workflow", tags=["Workflow"])


@router.post("/create-channel", response_model=WorkflowCreateChannelResponse, summary="Create Channel")
def create_channel(payload: WorkflowChannelCreate) -> WorkflowCreateChannelResponse:
    return workflow_service.create_channel(payload)


@router.post("/analyze-opportunity", response_model=WorkflowOpportunityResponse, summary="Analyze Opportunity")
def analyze_opportunity(payload: WorkflowStepRequest) -> WorkflowOpportunityResponse:
    return workflow_service.analyze_opportunity(payload)


@router.post("/generate-ideas", response_model=WorkflowIdeasResponse, summary="Generate Ideas")
def generate_ideas(payload: WorkflowStepRequest) -> WorkflowIdeasResponse:
    return workflow_service.generate_ideas(payload)


@router.post("/choose-idea", response_model=WorkflowSelectedIdeaResponse, summary="Choose Idea")
def choose_idea(payload: WorkflowChooseIdeaRequest) -> WorkflowSelectedIdeaResponse:
    return workflow_service.choose_idea(payload)


@router.post("/generate-hooks", response_model=WorkflowHooksResponse, summary="Generate Hooks")
def generate_hooks(payload: WorkflowStepRequest) -> WorkflowHooksResponse:
    return workflow_service.generate_hooks(payload)


@router.post("/choose-hook", response_model=WorkflowSelectedHookResponse, summary="Choose Hook")
def choose_hook(payload: WorkflowChooseHookRequest) -> WorkflowSelectedHookResponse:
    return workflow_service.choose_hook(payload)


@router.post("/generate-story", response_model=WorkflowStoryResponse, summary="Generate Story")
def generate_story(payload: WorkflowStepRequest) -> WorkflowStoryResponse:
    return workflow_service.generate_story(payload)


@router.post("/generate-production-plan", response_model=WorkflowProductionPlanResponse, summary="Generate Production Plan")
def generate_production_plan(payload: WorkflowStepRequest) -> WorkflowProductionPlanResponse:
    return workflow_service.generate_production_plan(payload)


@router.post("/ready-to-generate", response_model=WorkflowReadyResponse, summary="Ready To Generate")
def ready_to_generate(payload: WorkflowStepRequest) -> WorkflowReadyResponse:
    return workflow_service.ready_to_generate(payload)


@router.get("/{workflow_id}", response_model=WorkflowStateResponse, summary="Workflow State")
def get_workflow_state(workflow_id: str) -> WorkflowStateResponse:
    return workflow_service.get_state(workflow_id)
