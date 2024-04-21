import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.common.models import Base, IntegerIDMixIn
from src.app.school.models.student import Student
from src.app.school.models.professor import Professor


class Course(Base, IntegerIDMixIn):

    __tablename__ = "course"

    professor_id: Mapped[int] = mapped_column(sa.ForeignKey("professor.id", ondelete="SET NULL"), nullable=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    duration_value: Mapped[int] = mapped_column(nullable=False, index=True)
    duration_unit: Mapped[str] = mapped_column(nullable=False, index=True)

    professor: Mapped[Professor] = relationship(back_populates="courses")
    students: Mapped[list[Student]] = relationship(
        secondary="student_course",
        back_populates="courses",
        order_by=Student.name.asc(),
        cascade="save-update, merge, delete",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return f"Este es el curso {self.name}. Es impartida por el profesor {self.professor.name}."
