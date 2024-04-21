import sqlalchemy as sa
from sqlalchemy.orm import Session

from src.app.common.repository import BaseRepository
from src.app.school import models, schemas as sch, enums


class StudentRepository(BaseRepository[models.Student, sch.StudentCreateSch, sch.StudentUpdateSch]):

    model = models.Student

    def __init__(self, session: Session):
        self.session = session

    def get_all_stmt(self, name: str = None, career: enums.CareerEnum = None):
        filters = []
        if name is not None:
            stmt = filters.append(self.model.name.ilike(f"%{name}%"))
        if career is not None:
            stmt = filters.append(self.model.career == career)
        stmt = sa.select(self.model).where(*filters).order_by(self.model.name)
        return stmt

    def get_courses(self, student_id: int):
        stmt = (
            sa.select(models.Course)
            .join(models.StudentCourse)
            .where(models.StudentCourse.student_id == student_id)
            .order_by(models.Course.name)
        )
        return stmt
