import fastapi

from src.app.core.config.manager import settings
from src.app.movie import router as movie_router


router = fastapi.APIRouter()


@router.get("/", include_in_schema=False)
def docs():
    return fastapi.responses.RedirectResponse(url="/docs")


@router.get(
    f"{settings.API_V1_STR}/health",
    summary="Check service health",
    status_code=fastapi.status.HTTP_200_OK,
    tags=["health"],
)
async def health():
    return {
        "service": "API",
        "status": "OK",
    }


router.include_router(prefix=settings.API_V1_STR, router=movie_router)
