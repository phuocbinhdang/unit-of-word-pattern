from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructures.databases.schemas.base import Base, TimestampModifyTracking
from src.infrastructures.databases.schemas.user import User


class Post(TimestampModifyTracking, Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    content: Mapped[str] = mapped_column(String(255))
