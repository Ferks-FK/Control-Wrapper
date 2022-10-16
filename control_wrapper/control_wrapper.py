from typing import TYPE_CHECKING
from .errors import MissingParameter

#if TYPE_CHECKING:
from aiohttp import ClientSession, ClientTimeout, ServerTimeoutError
from .api import User


class ControlWrapper:
    async def __init__(self, url: str = None, api_key: str = None, timeout: float = 5.0, retries: int = 3):
        if url is None:
            raise MissingParameter("The parameter 'url' is required, that it is missing.")
        elif api_key is None:
            raise MissingParameter("The parameter 'api_key' is required, that it is missing.")
        
        if not url.endswith("/"):
            url += "/"

        self._session = ClientSession()

        self._url = url
        self._api_key = api_key
        #self._timeout = ClientTimeout(total=timeout)
        self._retries = retries

    @property
    def user(self):
        return User(self._url, self._api_key, self._session)