from typing import Annotated

from fastapi import Depends

from src.app.common.dependencies import DBSession
from src.app.school import models, repository, services


async def get_by_id(db: DBSession, student_id: int):
    student_repository = repository.StudentRepository(db=db)
    student_service = services.StudentService(repository=student_repository)
    return student_service.get_by_id_or_raise(id=student_id)


Student = Annotated[models.Student, Depends(get_by_id)]
