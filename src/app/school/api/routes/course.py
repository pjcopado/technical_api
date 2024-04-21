import fastapi
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate as sa_paginate

from src.app.school.api import dependencies as deps
from src.app.school import repository, services, schemas as sch, enums
from src.app.common.dependencies import DBSession


router = fastapi.APIRouter(prefix="/courses", tags=["[school] courses"])


@router.get(
    "",
    summary="get courses",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=Page[sch.CourseProfessorSch],
)
async def get_courses(
    session: DBSession,
    name: str = fastapi.Query(None, min_length=3),
):
    course_repository = repository.CourseRepository(session=session)
    course_service = services.CourseService(repository=course_repository)
    stmt = course_service.get_all_stmt(name=name)
    return sa_paginate(session, stmt)


@router.post("", summary="create course", status_code=fastapi.status.HTTP_201_CREATED, response_model=sch.CourseProfessorSch)
def create_course(
    session: DBSession,
    obj_in: sch.CourseCreateSch = fastapi.Body(...),
):
    course_repository = repository.CourseRepository(session=session)
    course_service = services.CourseService(repository=course_repository)
    return course_service.create(obj_in=obj_in)


@router.get(
    "/{course_id}",
    summary="get course by id",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=sch.CourseProfessorSch,
)
async def get_course(
    course: deps.Course,
):
    return course


@router.get(
    "/{course_id}/students",
    summary="get all students from course",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=Page[sch.StudentSch],
)
async def get_course(
    session: DBSession,
    course: deps.Course,
):
    course_repository = repository.CourseRepository(session=session)
    course_service = services.CourseService(repository=course_repository)
    stmt = course_service.get_students(course_id=course.id)
    return sa_paginate(session, stmt)


@router.post(
    "/{course_id}/students",
    summary="enroll student into course",
    status_code=fastapi.status.HTTP_201_CREATED,
)
def enroll_student(
    session: DBSession,
    course: deps.Course,
    obj_in: sch.CourseEnrollSch = fastapi.Body(...),
):
    student_repository = repository.StudentRepository(session=session)
    professor_repository = repository.ProfessorRepository(session=session)
    course_repository = repository.CourseRepository(session=session)
    course_service = services.CourseService(
        repository=course_repository, student_repository=student_repository, professor_repository=professor_repository
    )
    course_service.enroll_student(course_id=course.id, student_id=obj_in.student_id)
    return {"message": "Student enrolled successfully"}
