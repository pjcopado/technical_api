from typing import Annotated

from fastapi import Depends

from src.app.common.dependencies import DBSession
from src.app.school import models, repository, services


async def get_by_id(session: DBSession, professor_id: int):
    professor_repository = repository.ProfessorRepository(session=session)
    professor_service = services.ProfessorService(repository=professor_repository)
    return professor_service.get_by_id_or_raise(id=professor_id)


Professor = Annotated[models.Professor, Depends(get_by_id)]
