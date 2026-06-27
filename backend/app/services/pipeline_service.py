from dataclasses import asdict

from app.data.mock_store import STORE
from app.models.pipeline import PipelineRun, PipelineStep
from app.schemas.pipeline_schema import PipelineListResponse, PipelineRunResponse, PipelineStartRequest

PIPELINE_TEMPLATE = [
    ("Opportunity", "Trend AI", 45),
    ("Editorial", "Editorial Director AI", 60),
    ("Story", "Story Director AI", 75),
    ("Script", "Script AI", 90),
    ("Voice", "Voice AI", 80),
    ("Video", "Render AI", 180),
    ("Subtitles", "Subtitle AI", 60),
    ("Quality", "Quality Gate AI", 70),
    ("Schedule", "Scheduler AI", 40),
]


def list_pipeline_runs() -> PipelineListResponse:
    return PipelineListResponse(runs=[PipelineRunResponse(**asdict(run)) for run in STORE.pipeline_runs])


def start_pipeline(payload: PipelineStartRequest) -> PipelineRunResponse:
    steps = [
        PipelineStep(
            name=name,
            status="completed" if index < 3 else "simulated_pending",
            estimated_seconds=estimated_seconds,
            ai_owner=owner,
        )
        for index, (name, owner, estimated_seconds) in enumerate(PIPELINE_TEMPLATE)
    ]
    run = PipelineRun(
        topic=payload.topic,
        country=payload.country,
        language=payload.language,
        niche=payload.niche,
        steps=steps,
    )
    STORE.pipeline_runs.append(run)
    return PipelineRunResponse(**asdict(run))
