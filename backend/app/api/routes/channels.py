from fastapi import APIRouter, status

from app.schemas.channel_schema import ChannelCreate, ChannelResponse
from app.services import channel_service

router = APIRouter(prefix="/channels", tags=["Channels"])


@router.get("", response_model=list[ChannelResponse])
def get_channels() -> list[ChannelResponse]:
    return channel_service.list_channels()


@router.post("", response_model=ChannelResponse, status_code=status.HTTP_201_CREATED)
def post_channel(payload: ChannelCreate) -> ChannelResponse:
    return channel_service.create_channel(payload)
