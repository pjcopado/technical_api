import datetime

import pydantic


class OrmBaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        populate_by_name=True,
    )


class IntegerIDModelMixin(OrmBaseModel):
    id: int


class TimestampModelMixin(OrmBaseModel):
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
