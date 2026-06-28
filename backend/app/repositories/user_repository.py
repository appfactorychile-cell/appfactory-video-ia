from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.user import UserORM
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def get_by_email(self, email: str) -> UserORM | None:
        return self.db.scalar(select(UserORM).where(UserORM.email == email))

    def create(self, email: str, full_name: str, role: str = "owner") -> UserORM:
        user = UserORM(email=email, full_name=full_name, role=role, status="active")
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
