import datetime
from typing import Any

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped as Mapped, mapped_column as mapped_column
from sqlalchemy.sql import functions as sqlalchemy_functions


class DBTable(DeclarativeBase):

    id: Any
    created_at: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime(timezone=True), index=True, nullable=False, server_default=sqlalchemy_functions.now(), sort_order=999
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime(timezone=True), nullable=True, onupdate=sqlalchemy_functions.now(), sort_order=999
    )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


Base = DBTable


class IntegerIDMixIn(object):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, nullable=False, autoincrement=True, sort_order=-1)
