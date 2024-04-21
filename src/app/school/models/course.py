import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.common.models import Base, IntegerIDMixIn


class Course(Base, IntegerIDMixIn):

    __tablename__ = "course"

    professor_id: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey("professor.id"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    duration_value: Mapped[int] = mapped_column(nullable=False, index=True)
    duration_unit: Mapped[str] = mapped_column(nullable=False, index=True)

    professor = relationship("Professor", back_populates="courses")

    def __repr__(self) -> str:
        return f"Este es el curso {self.name}. Es impartida por el profesor {self.professor.name}."
