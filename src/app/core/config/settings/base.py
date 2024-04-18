import logging
import pathlib

from pydantic_settings import BaseSettings


ROOT_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.resolve()


class BackendBaseSettings(BaseSettings):
    SERVER_HOST: str = "127.0.0.1"
    SERVER_PORT: int = 8000

    # PROJECT INFO
    PROJECT_NAME: str = "ATAM"
    VERSION: str = "0.0.1"
    DESCRIPTION: str | None = None
    DEBUG: bool = True

    # APP SETTINGS
    ROOT_PATH: str = ""
    OPENAPI_URL: str | None = "/openapi.json"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    API_V1_STR: str = "/v1"

    # CORS
    IS_ALLOWED_CREDENTIALS: bool = True
    ALLOWED_ORIGINS: list[str] = ["localhost", "127.0.0.1", "*"]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]

    @property
    def set_backend_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `BackendBaseSettings`.
        """
        return {
            "title": self.PROJECT_NAME,
            "description": self.DESCRIPTION,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "root_path": self.ROOT_PATH,
            "contact": {
                "name": "ATAM",
                "url": "https://www.atam.es",
                "email": "pjcopado@gmail.com",
            },
            "swagger_ui_parameters": {
                "defaultModelsExpandDepth": -1,
                "defaultModelExpandDepth": 10,
            },
        }
