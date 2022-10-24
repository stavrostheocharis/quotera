from pydantic.main import BaseModel


class Error(Exception):
    """
    General exception
    """

    def __init__(self, *, detail: str):
        self.detail = detail
        super().__init__(self.detail)


class SystemError(Error):
    pass


class NotFoundError(Error):
    pass


class BadRequestError(Error):
    pass
