import fastapi

from src.app.core.config.manager import settings
from src.app.core.middlewares import register_middlewares
from src.app.core import exceptions
from src.app.api import router


def initialize_backend_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI(**settings.set_backend_app_attributes)

    register_middlewares(app)

    @app.exception_handler(exceptions.CustomError)
    async def custom_exceptions_handler(request: fastapi.Request, exc: exceptions.CustomError) -> fastapi.responses.JSONResponse:
        return fastapi.responses.JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
            headers=exc.headers,
        )

    app.include_router(router=router, prefix=settings.ROOT_PATH)

    return app


app: fastapi.FastAPI = initialize_backend_application()
