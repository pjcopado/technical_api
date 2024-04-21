__all__ = ["StudentCreateSch", "StudentUpdateSch", "StudentSch"]

import datetime

import pydantic

from src.app.common.schemas import OrmBaseModel, IntegerIDModelMixin
from src.app.school import enums


class StudentBaseSch(OrmBaseModel):
    name: str = pydantic.Field(..., min_length=3, max_length=64)
    career: enums.CareerEnum = pydantic.Field(...)


class StudentCreateSch(StudentBaseSch):
    birth_date: datetime.date = pydantic.Field(...)

    @pydantic.field_validator("birth_date")
    def age_range(cls, value: datetime.date) -> datetime.date:
        today = datetime.date.today()
        age = (today - value).days // 365
        if age < 18 or age > 99:
            raise ValueError("The student must be between 18 and 99 years old.")
        return value


class StudentUpdateSch(OrmBaseModel):
    name: str = pydantic.Field(None, min_length=3, max_length=64)
    career: str = pydantic.Field(None, min_length=3, max_length=64)
    birth_date: datetime.date = pydantic.Field(None)


class StudentSch(StudentBaseSch, IntegerIDModelMixin):
    age: int
