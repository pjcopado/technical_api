import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.app.core import exceptions
from src.app.common.repository import BaseRepository
from src.app.school import models, schemas as sch


class CourseRepository(BaseRepository[models.Course, sch.CourseCreateSch, sch.CourseUpdateSch]):

    model = models.Course

    def __init__(self, session: Session):
        self.session = session

    def get_all_stmt(self, name: str = None, professor_id: int = None):
        filters = []
        if name is not None:
            stmt = filters.append(self.model.name.ilike(f"%{name}%"))
        if professor_id is not None:
            stmt = filters.append(self.model.professor_id == professor_id)
        stmt = sa.select(self.model).where(*filters).order_by(self.model.name)
        return stmt

    def get_students(self, course_id: int):
        stmt = (
            sa.select(models.Student)
            .join(models.StudentCourse)
            .where(models.StudentCourse.course_id == course_id)
            .order_by(models.Student.name)
        )
        return stmt

    def enroll_student(self, course_id: int, student_id: int):
        obj_db = models.StudentCourse(course_id=course_id, student_id=student_id)
        self.session.add(obj_db)
        try:
            self.session.commit()
        except IntegrityError as e:
            self.session.rollback()
            raise exceptions.EntityAlreadyExists("Student already enrolled")
        self.session.refresh(obj_db)
        return obj_db
