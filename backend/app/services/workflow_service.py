from dataclasses import asdict
from datetime import datetime, timezone
from uuid import uuid4

from fastapi import HTTPException, status

from app.models.workflow import WorkflowChannel, WorkflowState
from app.schemas.content_brain_schema import ContentBrainRequest
from app.intelligence import global_intelligence
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
from app.services import content_brain_service

WORKFLOWS: dict[str, WorkflowState] = {}

PROGRESS_KEYS = [
    "channel",
    "opportunity",
    "ideas",
    "idea_selected",
    "hooks",
    "hook_selected",
    "story",
    "storyboard",
    "production",
    "ready",
]


def _progress(workflow: WorkflowState) -> dict[str, bool]:
    return {
        "channel": workflow.channel is not None,
        "opportunity": workflow.opportunity is not None,
        "ideas": bool(workflow.ideas),
        "idea_selected": workflow.selected_idea is not None,
        "hooks": bool(workflow.hooks),
        "hook_selected": workflow.selected_hook is not None,
        "story": workflow.story_strategy is not None,
        "storyboard": workflow.storyboard is not None,
        "production": workflow.production_plan is not None,
        "ready": workflow.ready,
    }


def _get(workflow_id: str) -> WorkflowState:
    workflow = WORKFLOWS.get(workflow_id)
    if workflow is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workflow not found")
    return workflow


def _touch(workflow: WorkflowState, step: str) -> None:
    workflow.current_step = step
    workflow.updated_at = datetime.now(timezone.utc)


def _brain_request(workflow: WorkflowState) -> ContentBrainRequest:
    return ContentBrainRequest(
        topic=workflow.channel.description,
        country=workflow.channel.country,
        language=workflow.channel.language,
        niche=workflow.channel.niche,
    )


def _channel_response(channel: WorkflowChannel) -> dict[str, object]:
    return asdict(channel)


def _base(workflow: WorkflowState) -> dict[str, object]:
    return {
        "workflow_id": workflow.id,
        "current_step": workflow.current_step,
        "progress": _progress(workflow),
    }


def create_channel(payload: WorkflowChannelCreate) -> WorkflowCreateChannelResponse:
    channel = WorkflowChannel(**payload.model_dump())
    workflow = WorkflowState(channel=channel)
    WORKFLOWS[workflow.id] = workflow
    return WorkflowCreateChannelResponse(
        **_base(workflow),
        channel=_channel_response(channel),
        created_at=workflow.created_at,
    )


def analyze_opportunity(payload: WorkflowStepRequest) -> WorkflowOpportunityResponse:
    workflow = _get(payload.workflow_id)
    brain_request = _brain_request(workflow)
    audit = global_intelligence.analyze_global_opportunity(
        topic=brain_request.topic,
        country=brain_request.country,
        language=brain_request.language,
        niche=brain_request.niche,
    )
    workflow.executive_audit = audit
    score = int(audit["opportunity_score"])
    workflow.opportunity = {
        "opportunity_score": score,
        "competition": audit["competition_analysis"]["competition_level"],
        "potential": "Alto" if score >= 82 else "Prometedor",
        "trend": audit["trend_analysis"]["trend_stage"],
        "monetization": f"{audit['roi_dashboard']['monetization_probability']}% de probabilidad mock",
        "ideal_time": "13:00 local time" if workflow.channel.mode == "manual" else "08:00 and 21:00 local time",
        "notes": audit["trend_analysis"]["signals"],
    }
    _touch(workflow, "opportunity_analyzed")
    return WorkflowOpportunityResponse(
        **_base(workflow),
        executive_decision=audit["executive_decision"],
        **workflow.opportunity,
    )


def generate_ideas(payload: WorkflowStepRequest) -> WorkflowIdeasResponse:
    workflow = _get(payload.workflow_id)
    if workflow.executive_audit is None:
        analyze_opportunity(payload)
    decision = workflow.executive_audit["executive_decision"] if workflow.executive_audit else {}
    if decision.get("decision") != "PRODUCIR":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Director Ejecutivo IA decidio {decision.get('decision', 'VOLVER A ANALIZAR')}. No se generan ideas todavia.",
        )
    analysis = content_brain_service.analyze(_brain_request(workflow))
    ideas: list[dict[str, object]] = []
    ranked_by_title = {item.title: item for item in analysis.ranking}
    for index, idea in enumerate(analysis.ideas, start=1):
        ranking = ranked_by_title.get(idea.title)
        curiosity = ranking.curiosity_score if ranking else 80 + index
        monetization = ranking.monetization_score if ranking else 78
        retention = min(96, curiosity - 3 + (index % 5))
        viral_level = round((curiosity + retention + monetization) / 3)
        ideas.append(
            {
                "id": f"idea-{index}",
                "title": idea.title,
                "curiosity": curiosity,
                "emotion": idea.emotion,
                "value": idea.value_promise,
                "viral_level": viral_level,
                "monetization": monetization,
                "retention": retention,
            }
        )
    workflow.ideas = ideas
    _touch(workflow, "ideas_generated")
    return WorkflowIdeasResponse(**_base(workflow), ideas=ideas)


def choose_idea(payload: WorkflowChooseIdeaRequest) -> WorkflowSelectedIdeaResponse:
    workflow = _get(payload.workflow_id)
    if not workflow.ideas:
        generate_ideas(WorkflowStepRequest(workflow_id=workflow.id))
    selected = next((idea for idea in workflow.ideas if idea["id"] == payload.idea_id), None)
    if selected is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Idea not found")
    workflow.selected_idea = selected
    _touch(workflow, "idea_selected")
    return WorkflowSelectedIdeaResponse(
        **_base(workflow),
        selected_idea=selected,
        message="Idea saved in the temporary workflow state.",
    )


def generate_hooks(payload: WorkflowStepRequest) -> WorkflowHooksResponse:
    workflow = _get(payload.workflow_id)
    if workflow.selected_idea is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Choose an idea before generating hooks")
    hooks = content_brain_service.analyze(_brain_request(workflow)).hooks
    workflow.hooks = [
        {
            "id": f"hook-{index}",
            "hook": hook.hook,
            "score": hook.score,
            "emotion": hook.emotion,
            "retention": hook.expected_retention,
        }
        for index, hook in enumerate(hooks, start=1)
    ]
    _touch(workflow, "hooks_generated")
    return WorkflowHooksResponse(**_base(workflow), hooks=workflow.hooks)


def choose_hook(payload: WorkflowChooseHookRequest) -> WorkflowSelectedHookResponse:
    workflow = _get(payload.workflow_id)
    if not workflow.hooks:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Generate hooks before choosing one")
    selected = next((hook for hook in workflow.hooks if hook["id"] == payload.hook_id), None)
    if selected is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hook not found")
    workflow.selected_hook = selected
    _touch(workflow, "hook_selected")
    return WorkflowSelectedHookResponse(
        **_base(workflow),
        selected_hook=selected,
        message="Hook saved in the temporary workflow state.",
    )


def generate_story(payload: WorkflowStepRequest) -> WorkflowStoryResponse:
    workflow = _get(payload.workflow_id)
    if workflow.selected_idea is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Choose an idea before generating story strategy")
    if workflow.selected_hook is None and workflow.hooks:
        workflow.selected_hook = workflow.hooks[0]
    brain = content_brain_service.analyze(_brain_request(workflow))
    storyboard = content_brain_service.storyboard(_brain_request(workflow))
    selected_title = str(workflow.selected_idea["title"])
    hook_text = workflow.selected_hook["hook"] if workflow.selected_hook else storyboard.hook
    scenes = [
        {
            "scene": "Scene 1",
            "visual": "Immediate problem frame with premium kinetic text.",
            "narration": f"{hook_text} This starts with a real question for {workflow.channel.country}.",
            "subtitles": "A practical problem appears immediately.",
        },
        {
            "scene": "Scene 2",
            "visual": "Localized example showing the selected idea in context.",
            "narration": f"The selected idea is: {selected_title}.",
            "subtitles": "The idea becomes concrete and local.",
        },
        {
            "scene": "Scene 3",
            "visual": "Comparison between doing nothing and using a simple strategy.",
            "narration": "We show the useful difference without promising impossible results.",
            "subtitles": "Useful, original and responsible.",
        },
        {
            "scene": "Scene 4",
            "visual": "Clean closing frame with CTA and safe publishing note.",
            "narration": "The final question invites comments without manipulating engagement.",
            "subtitles": "What would you test first?",
        },
    ]
    workflow.story_strategy = {
        "objective": "Turn one opportunity into a clear, useful and entertaining short video concept.",
        "narrator": brain.story_strategy.character,
        "character": "Relatable operator or creator facing the problem in a realistic environment.",
        "scenario": f"A realistic {workflow.channel.niche} workspace localized for {workflow.channel.country}.",
        "tone": brain.story_strategy.tone,
        "duration_seconds": brain.story_strategy.recommended_duration_seconds,
        "style": brain.story_strategy.visual_style,
    }
    workflow.storyboard = {
        "scenes": scenes,
        "narration": "Hook, local example, practical contrast and responsible CTA.",
        "subtitles": [scene["subtitles"] for scene in scenes],
        "cta": "What would you test first?",
    }
    _touch(workflow, "story_generated")
    return WorkflowStoryResponse(
        **_base(workflow),
        **workflow.story_strategy,
        scenes=scenes,
        narration=workflow.storyboard["narration"],
        subtitles=workflow.storyboard["subtitles"],
        cta=workflow.storyboard["cta"],
    )


def generate_production_plan(payload: WorkflowStepRequest) -> WorkflowProductionPlanResponse:
    workflow = _get(payload.workflow_id)
    if workflow.story_strategy is None:
        generate_story(payload)
    production = content_brain_service.production_plan(_brain_request(workflow))
    workflow.production_plan = {
        "narrator": production.narrator,
        "voice_type": "Natural, warm and platform-safe AI voice placeholder",
        "format": production.format,
        "platforms": workflow.channel.platforms or production.platforms,
        "music": production.music,
        "lighting": production.lighting,
        "camera_movement": "Slow push-in, quick cutaways and caption-led transitions",
        "color": "Dark premium base with cyan and green highlights",
        "rhythm": "Fast opening, steady explanation, crisp CTA",
        "duration_seconds": production.duration_seconds,
        "language": production.language,
    }
    _touch(workflow, "production_plan_generated")
    return WorkflowProductionPlanResponse(**_base(workflow), **workflow.production_plan)


def ready_to_generate(payload: WorkflowStepRequest) -> WorkflowReadyResponse:
    workflow = _get(payload.workflow_id)
    if workflow.production_plan is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Generate the production plan before marking ready")
    workflow.ready = True
    _touch(workflow, "ready_to_generate")
    return WorkflowReadyResponse(
        **_base(workflow),
        ready=True,
        message="Todo esta listo para generar el video.",
        next_locked_steps=["video_generation", "voice_generation", "image_generation", "publishing"],
    )


def get_state(workflow_id: str) -> WorkflowStateResponse:
    workflow = _get(workflow_id)
    return WorkflowStateResponse(
        **_base(workflow),
        channel=_channel_response(workflow.channel),
        opportunity=workflow.opportunity,
        executive_audit=workflow.executive_audit,
        ideas=workflow.ideas,
        selected_idea=workflow.selected_idea,
        hooks=workflow.hooks,
        selected_hook=workflow.selected_hook,
        story_strategy=workflow.story_strategy,
        storyboard=workflow.storyboard,
        production_plan=workflow.production_plan,
        ready=workflow.ready,
    )
