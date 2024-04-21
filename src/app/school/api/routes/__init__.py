import fastapi

from .careers import router as careers_router
from .student import router as student_router
from .professor import router as professor_router
from .course import router as course_router


router = fastapi.APIRouter()

router.include_router(router=careers_router)
router.include_router(router=student_router)
router.include_router(router=professor_router)
router.include_router(router=course_router)
