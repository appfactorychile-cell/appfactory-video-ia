from sqlalchemy.orm import Session

from app.database.models.channel import ChannelORM
from app.repositories import ChannelRepository
from app.schemas.channel_schema import ChannelCreate, ChannelResponse


def _to_response(channel: ChannelORM) -> ChannelResponse:
    return ChannelResponse(
        id=channel.id,
        name=channel.name,
        target_country=channel.target_country,
        language=channel.language,
        timezone=channel.timezone,
        niche=channel.niche,
        visual_style=channel.visual_style,
        ai_voice=channel.ai_voice,
        daily_video_count=channel.daily_video_count,
        publishing_times=channel.publishing_times,
        connected_platforms=channel.connected_platforms,
        content_rules=channel.content_rules,
        status=channel.status,
        created_at=channel.created_at,
    )


def list_channels(db: Session) -> list[ChannelResponse]:
    return [_to_response(channel) for channel in ChannelRepository(db).list()]


def create_channel(payload: ChannelCreate, db: Session) -> ChannelResponse:
    channel = ChannelRepository(db).create(**payload.model_dump())
    return _to_response(channel)
