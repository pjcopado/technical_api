import sqlalchemy as sa
from sqlalchemy.orm import Session

from src.app.common.repository import BaseRepository
from src.app.school import models, schemas as sch, enums


class ProfessorRepository(BaseRepository[models.Professor, sch.ProfessorCreateSch, sch.ProfessorUpdateSch]):

    model = models.Professor

    def __init__(self, session: Session):
        self.session = session

    def get_all_stmt(self, name: str = None, age_ge: int = None, age_le: int = None, specialty: enums.CareerEnum = None):
        filters = []
        if name is not None:
            stmt = filters.append(self.model.name.ilike(f"%{name}%"))
        if age_ge is not None:
            stmt = filters.append(self.model.age >= age_ge)
        if age_le is not None:
            stmt = filters.append(self.model.age <= age_le)
        if specialty is not None:
            stmt = filters.append(self.model.specialty == specialty)
        stmt = sa.select(self.model).where(*filters).order_by(self.model.name)
        return stmt

    def get_courses(self, professor_id: int):
        stmt = sa.select(models.Course).where(models.Course.professor_id == professor_id).order_by(models.Course.name)
        return stmt
