import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from src.app.common.models import Base, IntegerIDMixIn


class Student(Base, IntegerIDMixIn):

    __tablename__ = "student"

    name: Mapped[str] = mapped_column(nullable=False, index=True)
    birth_date: Mapped[datetime.date] = mapped_column(nullable=False, index=True)
    career: Mapped[str] = mapped_column(nullable=False, index=True)

    @hybrid_property
    def age(self):
        today = datetime.date.today()
        return (today - self.birth_date).days // 365

    @age.expression
    def age(cls):
        return (
            sa.func.strftime("%Y", "now")
            - sa.func.strftime("%Y", cls.birth_date)
            - ((sa.func.strftime("%m-%d", "now") < sa.func.strftime("%m-%d", cls.birth_date)))
        )

    courses = relationship(
        "Course",
        secondary="student_course",
        back_populates="students",
        order_by="Course.name",
        cascade="save-update, merge, delete",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return f"Hola, soy {self.name}, tengo {self.age} años y estudio {self.career}."
