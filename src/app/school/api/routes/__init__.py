import fastapi

from .careers import router as careers_router
from .student import router as student_router


router = fastapi.APIRouter()

router.include_router(router=careers_router)
router.include_router(router=student_router)
