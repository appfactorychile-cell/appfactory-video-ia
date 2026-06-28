from app.database.base import Base
from app.database.database import engine
from app.database.models import *  # noqa: F401,F403


def init_database() -> None:
    Base.metadata.create_all(bind=engine)
