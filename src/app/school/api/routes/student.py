import fastapi
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate as sa_paginate

from src.app.school.api import dependencies as deps
from src.app.school import repository, services, schemas as sch, enums
from src.app.common.dependencies import DBSession


router = fastapi.APIRouter(prefix="/students", tags=["[school] students"])


@router.get(
    "",
    summary="get students",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=Page[sch.StudentSch],
)
async def get_student(
    db: DBSession,
    name: str = fastapi.Query(None, min_length=3),
    career: enums.CareerEnum = fastapi.Query(None),
):
    student_repository = repository.StudentRepository(db=db)
    student_service = services.StudentService(repository=student_repository)
    stmt = student_service.get_all_stmt(name=name, career=career)
    return sa_paginate(db, stmt)


@router.post("", summary="create student", status_code=fastapi.status.HTTP_201_CREATED, response_model=sch.StudentSch)
def create_student(
    db: DBSession,
    obj_in: sch.StudentCreateSch = fastapi.Body(...),
):
    student_repository = repository.StudentRepository(db=db)
    student_service = services.StudentService(repository=student_repository)
    return student_service.create(obj_in=obj_in)


@router.get(
    "/{student_id}",
    summary="get student by id",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=sch.StudentSch,
)
async def get_student(
    db: DBSession,
    student: deps.Student,
):
    return student


@router.get(
    "/{student_id}/courses",
    summary="get all courses from student",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=Page[sch.CourseSch],
)
async def get_student_courses(
    db: DBSession,
    student: deps.Student,
):
    student_repository = repository.StudentRepository(db=db)
    student_service = services.StudentService(repository=student_repository)
    stmt = student_service.get_courses(student_id=student.id)
    return sa_paginate(db, stmt)
