from typing import Generic, Type, TypeVar

import pydantic
import sqlalchemy as sa
from sqlalchemy.orm import Session

from src.app.core import exceptions
from src.app.common.models import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=pydantic.BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=pydantic.BaseModel)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    model: Type[ModelType]

    def __init__(self, session: Session):
        self.session = session

    def get_all_stmt(self, **kwargs):
        stmt = sa.select(self.model).where(*kwargs).order_by(self.model.created_at.asc())
        return stmt

    def get_by_id(self, id: int) -> ModelType | None:
        stmt = sa.select(self.model).where(self.model.id == id)
        query = self.session.execute(stmt)
        return query.scalar()

    def get_by_id_or_raise(self, id: int) -> ModelType:
        record = self.get_by_id(id)
        if not record:
            raise exceptions.EntityDoesNotExist(f"{self.model.__name__} with {id=} does not exist")
        return record

    def get_by_attributes(self, **kwargs) -> ModelType | None:
        stmt = sa.select(self.model)
        for attr, value in kwargs.items():
            stmt = stmt.where(getattr(self.model, attr) == value)
        stmt = stmt.order_by(self.model.created_at.asc())
        query = self.session.execute(stmt)
        return query.scalar()

    def get_by_attributes_or_raise(self, **kwargs) -> ModelType:
        record = self.get_by_attributes(**kwargs)
        if not record:
            raise exceptions.EntityDoesNotExist(f"{self.model.__name__} with attributes {kwargs} does not exist")
        return record

    def create(self, *, obj_in: CreateSchemaType | dict, **kwargs) -> ModelType:
        if isinstance(obj_in, dict):
            obj_in_dict = obj_in
        else:
            obj_in_dict = obj_in.model_dump()
        obj_db = self.model(**obj_in_dict, **kwargs)
        self.session.add(obj_db)
        self.session.commit()
        self.session.refresh(obj_db)
        return obj_db

    def update(
        self,
        *,
        obj_db: ModelType,
        obj_in: UpdateSchemaType | dict,
        **kwargs,
    ) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        update_data = {**update_data, **kwargs}
        for field, value in update_data.items():
            if hasattr(obj_db, field) and not isinstance(value, dict):
                setattr(obj_db, field, value)
        self.session.commit()
        self.session.refresh(obj_db)
        return obj_db

    def delete(self, *, obj_db: ModelType) -> ModelType:
        self.session.delete(obj_db)
        self.session.commit()
        return obj_db
