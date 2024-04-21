import sqlalchemy as sa
from sqlalchemy.orm import Session

from src.app.school import schemas as sch
from src.app.core import exceptions
from src.app.school import models


class CourseRepository:

    model = models.Course

    def __init__(self, db: Session):
        self.db = db

    def get_all_stmt(self, name: list[str] = None, professor_id: int = None):
        filters = []
        if name is not None:
            stmt = filters.append(self.model.name.in_(name))
        if professor_id is not None:
            stmt = filters.append(self.model.professor_id == professor_id)
        stmt = sa.select(self.model).filter(*filters).order_by(self.model.name)
        return stmt

    def get_by_id(self, id: int):
        stmt = sa.select(self.model).filter(self.model.id == id)
        query = self.db.execute(stmt)
        return query.scalar()

    def get_by_id_or_raise(self, id: int) -> model:
        record = self.get_by_id(id)
        if not record:
            raise exceptions.CustomError(status_code=404, detail="Course does not exist")
        return record

    def get_students(self, course_id: int):
        stmt = (
            sa.select(models.Student)
            .join(models.StudentCourse)
            .where(models.StudentCourse.course_id == course_id)
            .order_by(models.Student.name)
        )
        return stmt

    def create(self, obj_in: sch.CourseCreateSch):
        obj_db = self.model(**obj_in.model_dump())
        self.db.add(obj_db)
        self.db.commit()
        self.db.refresh(obj_db)
        return obj_db

    def enroll_student(self, course_id: int, student_id: int):
        obj_db = models.StudentCourse(course_id=course_id, student_id=student_id)
        self.db.add(obj_db)
        self.db.commit()
        self.db.refresh(obj_db)
        return obj_db
