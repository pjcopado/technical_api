__all__ = ["CourseCreateSch", "CourseUpdateSch", "CourseEnrollSch", "CourseSch", "CourseProfessorSch"]

import pydantic

from .professor import ProfessorSch
from src.app.common.schemas import OrmBaseModel, IntegerIDModelMixin
from src.app.school import enums


class CourseBaseSch(OrmBaseModel):
    name: str = pydantic.Field(..., min_length=3, max_length=64)
    duration_value: int = pydantic.Field(..., ge=1)
    duration_unit: enums.CourseDurationUnitEnum = pydantic.Field(...)


class CourseCreateSch(CourseBaseSch):
    professor_id: int | None = pydantic.Field(...)


class CourseUpdateSch(OrmBaseModel):
    name: str = pydantic.Field(None, min_length=3, max_length=64)
    duration_value: int = pydantic.Field(None, ge=1)
    duration_unit: enums.CourseDurationUnitEnum = pydantic.Field(None)


class CourseEnrollSch(OrmBaseModel):
    student_id: int = pydantic.Field(...)


class CourseSch(CourseBaseSch, IntegerIDModelMixin):
    pass


class CourseProfessorSch(CourseBaseSch, IntegerIDModelMixin):
    professor: ProfessorSch | None
