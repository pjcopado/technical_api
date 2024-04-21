import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.app.common.models import Base


class StudentCourse(Base):

    __tablename__ = "student_course"

    course_id: Mapped[int] = mapped_column(
        sa.ForeignKey("course.id", ondelete="CASCADE"), primary_key=True, nullable=False, index=True
    )
    student_id: Mapped[int] = mapped_column(
        sa.ForeignKey("student.id", ondelete="CASCADE"), primary_key=True, nullable=False, index=True
    )
