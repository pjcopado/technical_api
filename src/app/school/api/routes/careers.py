import fastapi

from src.app.school import enums


router = fastapi.APIRouter(prefix="/careers", tags=["[school] careers"])


@router.get("", summary="get careers", status_code=fastapi.status.HTTP_200_OK, response_model=list[str])
def get_careers():
    return enums.CareerEnum.to_list()
