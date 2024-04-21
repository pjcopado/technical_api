__all__ = ["ProfessorCreateSch", "ProfessorUpdateSch", "ProfessorSch"]

import datetime
import pydantic

from src.app.school import enums
from src.app.common.schemas import OrmBaseModel, IntegerIDModelMixin


class ProfessorBaseSch(OrmBaseModel):
    name: str = pydantic.Field(..., min_length=3, max_length=64)
    specialty: enums.CareerEnum = pydantic.Field(..., min_length=3, max_length=64)


class ProfessorCreateSch(ProfessorBaseSch):
    birth_date: datetime.date = pydantic.Field(...)

    @pydantic.field_validator("birth_date")
    def age_range(cls, value: datetime.date) -> datetime.date:
        today = datetime.date.today()
        age = (today - value).days // 365
        if age < 18 or age > 99:
            raise ValueError("The professor must be between 18 and 99 years old.")
        return value


class ProfessorUpdateSch(OrmBaseModel):
    name: str = pydantic.Field(None, min_length=3, max_length=64)
    specialty: enums.CareerEnum = pydantic.Field(None, min_length=3, max_length=64)
    birth_date: datetime.date = pydantic.Field(None)


class ProfessorSch(ProfessorBaseSch, IntegerIDModelMixin):
    age: int
