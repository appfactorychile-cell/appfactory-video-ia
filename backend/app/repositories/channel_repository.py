from sqlalchemy import select

from app.database.models.channel import ChannelORM
from app.repositories.base_repository import BaseRepository


class ChannelRepository(BaseRepository):
    def list(self) -> list[ChannelORM]:
        return list(self.db.scalars(select(ChannelORM).order_by(ChannelORM.created_at.desc())))

    def create(self, **data) -> ChannelORM:
        channel = ChannelORM(**data, status="active")
        self.db.add(channel)
        self.db.commit()
        self.db.refresh(channel)
        return channel
