from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructures.databases.schemas.base import Base, TimestampModifyTracking


class User(TimestampModifyTracking, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), index=True, unique=True)
    password: Mapped[str] = mapped_column(String(255))
