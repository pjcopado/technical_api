import sqlalchemy as sa
from sqlalchemy.orm import Session

from src.app.core import exceptions
from src.app.school import models, schemas as sch, enums


class ProfessorRepository:

    model = models.Professor

    def __init__(self, db: Session):
        self.db = db

    def get_all_stmt(self, name: str = None, age_ge: int = None, age_le: int = None, specialty: enums.CareerEnum = None):
        filters = []
        if name is not None:
            stmt = filters.append(self.model.name.ilike(f"%{name}%"))
        if age_ge is not None:
            stmt = filters.append(self.model.age >= age_ge)
        if age_le is not None:
            stmt = filters.append(self.model.age <= age_le)
        stmt = sa.select(self.model).filter(*filters).order_by(self.model.name)
        if specialty is not None:
            stmt = stmt.filter(self.model.specialty == specialty)
        return stmt

    def get_by_id(self, id: int):
        stmt = sa.select(self.model).filter(self.model.id == id)
        query = self.db.execute(stmt)
        return query.scalar()

    def get_by_id_or_raise(self, id: int) -> model:
        record = self.get_by_id(id)
        if not record:
            raise exceptions.CustomError(status_code=404, detail="Professor does not exist")
        return record

    def create(self, obj_in: sch.StudentCreateSch):
        obj_db = self.model(**obj_in.model_dump())
        self.db.add(obj_db)
        self.db.commit()
        self.db.refresh(obj_db)
        return obj_db

    def get_courses(self, professor_id: int):
        stmt = sa.select(models.Course).where(models.Course.professor_id == professor_id).order_by(models.Course.name)
        return stmt
