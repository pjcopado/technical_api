from starlette import status


class CustomError(Exception):
    """Base class for all errors raised by the App.

    Args:
        detail: A human-readable error detail string.
        status_code: int. The HTTP status code
        cause: The exception that caused this error (optional).
        headers: dict[str, Any] | None. The HTTP headers (optional).
    """

    def __init__(
        self,
        detail: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        headers: dict | None = None,
    ):
        Exception.__init__(self, detail)
        self.detail = detail
        self.status_code = status_code
        self.headers = headers
