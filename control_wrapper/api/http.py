from typing import TYPE_CHECKING, Any
from ..errors import MissingParameter, MaxRetriesExeption

#if TYPE_CHECKING:
from aiohttp import ClientSession, ClientTimeout, ServerTimeoutError
from aiohttp.http_exceptions import BadHttpMessage

class HTTPClient:
    def __init__(self, url: str = None, api_key: str = None, session: ClientSession = None):
        self._url = url
        self._api_key = api_key
        self._session = session
        self._headers = {
            "Authorization": "Bearer " + api_key,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        print(url, api_key, session)
        
    async def _make_request(self, endpoint: str = None, method: str = "GET", **kwargs: Any):
        endpoint_url = self._url + endpoint

        try:
            async with self._session.request(method=method, url=endpoint_url, headers=self._headers, **kwargs) as response:
                await response.close()

        except ServerTimeoutError:
            raise ServerTimeoutError("The connection to the server '{self._url}' took too long to respond.", self._url)
        except Exception as e:
            print(e)
        else:
            return response.json()
        
        
            