__all__ = ["ProfessorCreateSch", "ProfessorUpdateSch", "ProfessorSch"]

import datetime
import pydantic

from src.app.school import enums
from src.app.common.schemas import OrmBaseModel


class ProfessorBaseSch(OrmBaseModel):
    name: str = pydantic.Field(..., min_length=3, max_length=64)
    specialty: enums.CareerEnum = pydantic.Field(..., min_length=3, max_length=64)


class ProfessorCreateSch(ProfessorBaseSch):
    birth_date: datetime.date = pydantic.Field(...)


class ProfessorUpdateSch(OrmBaseModel):
    name: str = pydantic.Field(None, min_length=3, max_length=64)
    specialty: enums.CareerEnum = pydantic.Field(None, min_length=3, max_length=64)
    birth_date: datetime.date = pydantic.Field(None)


class ProfessorSch(ProfessorCreateSch):
    id: int

    """
    @pydantic.computed_field
    @property
    def age(self) -> int:
        return (datetime.date.today() - self.birth_date).days // 365
    """