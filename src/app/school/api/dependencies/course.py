from typing import Annotated

from fastapi import Depends

from src.app.common.dependencies import DBSession
from src.app.school import models, repository, services


async def get_by_id(session: DBSession, course_id: int):
    course_repository = repository.CourseRepository(session=session)
    course_service = services.CourseService(repository=course_repository)
    return course_service.get_by_id_or_raise(id=course_id)


Course = Annotated[models.Course, Depends(get_by_id)]
