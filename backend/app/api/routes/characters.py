from fastapi import APIRouter
from pydantic import BaseModel

from app.characters.character_engine import animate, assign_character, character_detail, library, list_characters


router = APIRouter(prefix="/characters", tags=["Character Animation Engine"])


class CharacterAssignRequest(BaseModel):
    scene_id: str = "composed-scene-1"
    character_id: str = "narrador-hombre"
    expression: str = "Feliz"
    pose: str = "Explicando"
    animation: str = "Hablar"


class CharacterAnimateRequest(BaseModel):
    scene_id: str = "composed-scene-1"
    character_id: str = "narrador-hombre"
    text: str = "La IA explica una idea de tecnologia y negocio."
    expression: str = "Feliz"
    pose: str = ""
    animation: str = "Hablar"


@router.get("", summary="Characters")
def characters() -> list[dict[str, object]]:
    return list_characters()


@router.get("/library", summary="Character Library")
def character_library() -> dict[str, object]:
    return library()


@router.get("/{character_id}", summary="Character Detail")
def character(character_id: str) -> dict[str, object]:
    return character_detail(character_id)


@router.post("/assign", summary="Assign Character To Scene")
def assign(payload: CharacterAssignRequest) -> dict[str, object]:
    return assign_character(payload.model_dump())


@router.post("/animate", summary="Animate Character")
def animate_endpoint(payload: CharacterAnimateRequest) -> dict[str, object]:
    return animate(payload.model_dump())
