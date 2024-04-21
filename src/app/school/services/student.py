import sqlalchemy as sa
from sqlalchemy.orm import Session

from src.app.school import schemas as sch, enums
from src.app.core import exceptions
from src.app.school import models


class StudentService:

    model = models.Student

    def __init__(self, db: Session):
        self.db = db

    def get_all_stmt(self, name: str = None):
        filters = []
        if name is not None:
            stmt = filters.append(self.model.name.ilike(f"%{name}%"))
        stmt = sa.select(self.model).filter(*filters).order_by(self.model.name)
        return stmt

    def create(self, obj_in: sch.StudentCreateSch):
        obj_db = self.model(**obj_in.model_dump())
        self.db.add(obj_db)
        self.db.commit()
        self.db.refresh(obj_db)
        return obj_db
