"SQLAlchemy ORM models"

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from services.database import Base

class Meme(Base):
    "Meme model"
    __tablename__ = "meme"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    file: Mapped[str] = mapped_column(nullable=False)
    uploaded_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())

    def __str__(self) -> str:
        return self.title
