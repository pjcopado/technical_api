import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from src.app.common.models import Base, IntegerIDMixIn
from src.app.school.models.course import Course


class Professor(Base, IntegerIDMixIn):

    __tablename__ = "professor"

    name: Mapped[str] = mapped_column(nullable=False, index=True)
    birth_date: Mapped[datetime.date] = mapped_column(nullable=False, index=True)
    specialty: Mapped[str] = mapped_column(nullable=False, index=True)

    @hybrid_property
    def age(self):
        today = datetime.date.today()
        return (today - self.birth_date).days // 365

    courses: Mapped[list[Course]] = relationship(back_populates="professor")

    def __repr__(self) -> str:
        return f"Hola, soy el profesor {self.name}, tengo {self.age} años e imparto las asignaturas {', '.join(self.courses)}."
