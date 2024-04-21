import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
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

    def __repr__(self) -> str:
        return f"Hola, soy {self.name}, tengo {self.age} años y estudio {self.career}."
