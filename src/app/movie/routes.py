import fastapi

from . import schemas as sch, services


router = fastapi.APIRouter(prefix="/movies", tags=["[movies] movies"])


@router.post(
    "",
    summary="upload movies",
    status_code=fastapi.status.HTTP_201_CREATED,
    response_model=list[sch.Movie],
)
def upload_movies(
    list_obj_in: list[sch.MovieCreate] = fastapi.Body(...),
):
    movie_service = services.MovieService()
    return movie_service.create_bulk(list_obj_in=list_obj_in)
