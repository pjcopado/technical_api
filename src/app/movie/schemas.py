import pydantic

from . import enums, utils
from src.app.common.schemas import OrmBaseModel


# habría que saber por modelo de negocio si algunos de los campos podrían ser nulos
# en principio como no veo ninguno en los listados no lo considero
class MovieBase(OrmBaseModel):
    name: str = pydantic.Field(..., title="Movie Name", description="Name of the movie")
    director: str = pydantic.Field(..., title="Movie Director", description="Director of the movie")
    ost: str = pydantic.Field(..., title="OST", description="Original Sound Track of the movie")
    actors: list[str] = pydantic.Field(default_factory=list, title="Actors", description="List of actors in the movie")
    synopsis: str = pydantic.Field(..., title="Synopsis", description="Synopsis of the movie")
    ratings: dict[enums.RatingWebsiteEnum, float] = pydantic.Field(
        default_factory=dict, title="Ratings", description="Ratings of the movie"
    )


class MovieCreate(MovieBase):
    pass

    @pydantic.field_validator("synopsis")
    def clean_text(cls, value: str) -> str:
        return utils.clean_text(value)


class Movie(MovieBase):
    rating_mean: float = pydantic.Field(..., title="Rating Mean", description="Mean of the ratings of the movie")
