__all__ = ["CourseCreateSch", "CourseSch"]

import pydantic

from .professor import ProfessorSch
from src.app.common.schemas import OrmBaseModel


class CourseBaseSch(OrmBaseModel):
    name: str = pydantic.Field(..., min_length=3, max_length=64)
    duration_value: int = pydantic.Field(..., ge=1)
    duration_unit: str = pydantic.Field(..., min_length=1, max_length=16)


class CourseCreateSch(CourseBaseSch):
    professor_id: int = pydantic.Field(...)


class CourseSch(CourseBaseSch):
    professor: ProfessorSch
