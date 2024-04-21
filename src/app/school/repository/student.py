import sqlalchemy as sa
from sqlalchemy.orm import Session

from src.app.school import schemas as sch, enums
from src.app.school import models


class StudentRepository:

    model = models.Student

    def __init__(self, db: Session):
        self.db = db

    def get_all_stmt(self, name: str = None, career: enums.CareerEnum = None):
        filters = []
        if name is not None:
            stmt = filters.append(self.model.name.ilike(f"%{name}%"))
        if career is not None:
            stmt = filters.append(self.model.career == career)
        stmt = sa.select(self.model).where(*filters).order_by(self.model.name)
        return stmt

    def get_by_id(self, id: int):
        stmt = sa.select(self.model).where(self.model.id == id)
        query = self.db.execute(stmt)
        return query.scalar()

    def create(self, obj_in: sch.StudentCreateSch):
        obj_db = self.model(**obj_in.model_dump())
        self.db.add(obj_db)
        self.db.commit()
        self.db.refresh(obj_db)
        return obj_db

    def get_courses(self, student_id: int):
        stmt = (
            sa.select(models.Course)
            .join(models.StudentCourse)
            .where(models.StudentCourse.student_id == student_id)
            .order_by(models.Course.name)
        )
        return stmt
