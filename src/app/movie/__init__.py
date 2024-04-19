import fastapi

from .routes import router as movie_router


router = fastapi.APIRouter()

router.include_router(router=movie_router)
