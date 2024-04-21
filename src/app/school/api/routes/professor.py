import fastapi
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate as sa_paginate

from src.app.school.api import dependencies as deps
from src.app.school import repository, services, schemas as sch, enums
from src.app.common.dependencies import DBSession


router = fastapi.APIRouter(prefix="/professors", tags=["[school] professors"])


@router.get(
    "",
    summary="get professors",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=Page[sch.ProfessorSch],
)
async def get_professor(
    session: DBSession,
    name: str = fastapi.Query(None, min_length=3),
    age_ge: int = fastapi.Query(None),
    age_le: int = fastapi.Query(None),
    specialty: enums.CareerEnum = fastapi.Query(None),
):
    if age_le is not None and age_ge is not None and age_ge > age_le:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail="age_ge must be less than or equal to age_le"
        )
    professor_repository = repository.ProfessorRepository(session=session)
    professor_service = services.ProfessorService(repository=professor_repository)
    stmt = professor_service.get_all_stmt(name=name, age_ge=age_ge, age_le=age_le, specialty=specialty)
    return sa_paginate(session, stmt)


@router.post("", summary="create professor", status_code=fastapi.status.HTTP_201_CREATED, response_model=sch.ProfessorSch)
def create_professor(
    session: DBSession,
    obj_in: sch.ProfessorCreateSch = fastapi.Body(...),
):
    professor_repository = repository.ProfessorRepository(session=session)
    professor_service = services.ProfessorService(repository=professor_repository)
    return professor_service.create(obj_in=obj_in)


@router.get(
    "/{professor_id}",
    summary="get professor by id",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=sch.ProfessorSch,
)
async def get_professor(
    professor: deps.Professor,
):
    return professor


@router.get(
    "/{professor_id}/courses",
    summary="get all courses from professor",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=Page[sch.CourseSch],
)
async def get_professor_courses(
    session: DBSession,
    professor: deps.Professor,
):
    professor_repository = repository.ProfessorRepository(session=session)
    professor_service = services.ProfessorService(repository=professor_repository)
    stmt = professor_service.get_courses(professor_id=professor.id)
    return sa_paginate(session, stmt)
