import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from src.app.common.models import Base, IntegerIDMixIn


class Professor(Base, IntegerIDMixIn):

    __tablename__ = "professor"

    name: Mapped[str] = mapped_column(nullable=False, index=True)
    birth_date: Mapped[datetime.date] = mapped_column(nullable=False, index=True)
    specialty: Mapped[str] = mapped_column(nullable=False, index=True)

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

    courses = relationship("Course", back_populates="professor")

    def __repr__(self) -> str:
        if self.courses:
            return f"Hola, soy el profesor {self.name}, tengo {self.age} años e imparto las asignaturas: {', '.join([course.name for course in self.courses])}."
        return f"Hola, soy el profesor {self.name}, tengo {self.age} años y actualmente no imparto asignaturas."
