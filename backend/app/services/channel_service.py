from dataclasses import asdict

from app.data.mock_store import STORE
from app.models.channel import Channel
from app.schemas.channel_schema import ChannelCreate, ChannelResponse


def list_channels() -> list[ChannelResponse]:
    return [ChannelResponse(**asdict(channel)) for channel in STORE.channels]


def create_channel(payload: ChannelCreate) -> ChannelResponse:
    channel = Channel(**payload.model_dump())
    STORE.channels.append(channel)
    return ChannelResponse(**asdict(channel))
