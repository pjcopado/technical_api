from src.app.core.config.settings.base import BackendBaseSettings
from src.app.core.config.settings.environment import Environment


class BackendLocalSettings(BackendBaseSettings):
    ENVIRONMENT: Environment = Environment.LOCAL
    DESCRIPTION: str | None = "Local Environment 🏠"
    DEBUG: bool = True
