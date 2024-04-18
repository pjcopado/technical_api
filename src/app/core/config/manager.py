from functools import lru_cache

from .settings import (
    Environment,
    BackendBaseSettings,
    BackendLocalSettings,
)


class BackendSettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> BackendBaseSettings:
        return {
            Environment.LOCAL: BackendLocalSettings,
        }.get(self.environment, BackendLocalSettings)()


@lru_cache()
def get_settings() -> BackendBaseSettings:
    return BackendSettingsFactory(environment=Environment.LOCAL)()  # type: ignore


settings: BackendBaseSettings = get_settings()
