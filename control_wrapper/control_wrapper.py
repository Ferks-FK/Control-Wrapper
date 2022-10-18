from typing import TYPE_CHECKING
from .errors import MissingParameter

#if TYPE_CHECKING:
from aiohttp import ClientSession, ClientTimeout, ServerTimeoutError
from .api import User


class ControlWrapper:
    def __init__(self, url: str = None, token: str = None):
        if url is None:
            raise MissingParameter("The parameter 'url' is required, that it is missing.")
        elif token is None:
            raise MissingParameter("The parameter 'api_key' is required, that it is missing.")
        
        if not url.endswith("/"):
            url += "/"

        self._url = url
        self._token = token

    @property
    def user(self):
        return User(self._token, self._url)