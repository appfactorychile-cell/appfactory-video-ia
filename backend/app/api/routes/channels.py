from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.channel_schema import ChannelCreate, ChannelResponse
from app.services import channel_service

router = APIRouter(prefix="/channels", tags=["Channels"])


@router.get("", response_model=list[ChannelResponse])
def get_channels(db: Session = Depends(get_db)) -> list[ChannelResponse]:
    return channel_service.list_channels(db)


@router.post("", response_model=ChannelResponse, status_code=status.HTTP_201_CREATED)
def post_channel(payload: ChannelCreate, db: Session = Depends(get_db)) -> ChannelResponse:
    return channel_service.create_channel(payload, db)
