from typing import Dict, Optional
from ..errors import HTTPException

#if TYPE_CHECKING:
from aiohttp import ClientSession, ClientResponse



class HTTPClient:
    def __init__(self, token: str, url: str) -> None:
        self.token = token
        self.url = url
        headers: Dict[str, str] = {
            "Authorization": "Bearer " + self.token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.__session: ClientSession = ClientSession(headers=headers)
    
    async def close(self) -> None:
        if self.__session:
            await self.__session.close()
    
    async def request(self, method: str, endpoint: str, kwargs):
        base_endpoint = self.url + endpoint
        response: Optional[ClientResponse] = None

        print(kwargs, "PRIMEIRO REQUEST")

        async with self.__session.request(method, base_endpoint, json=kwargs) as response:
            print(method, "SEGUNDO REQUEST")
            response_json = await response.json()
            await self.close()

            if response.status == 200:
                return response_json
            
            raise HTTPException(f"Could not query the API. Code: {response.status}.")















# class HTTPClient:
#     def __init__(self, url: str = None, api_key: str = None, session: ClientSession = None):
#         self._url = url
#         self._api_key = api_key
#         self._session = session
#         self._headers = {
#             "Authorization": "Bearer " + api_key,
#             "Accept": "application/json",
#             "Content-Type": "application/json"
#         }
#         print(url, api_key, session)
        
#     async def _make_request(self, endpoint: str = None, method: str = "GET", **kwargs: Any):
#         endpoint_url = self._url + endpoint

#         try:
#             async with self._session.request(method=method, url=endpoint_url, headers=self._headers, **kwargs) as response:
#                 await response.close()

#         except ServerTimeoutError:
#             raise ServerTimeoutError("The connection to the server '{self._url}' took too long to respond.", self._url)
#         except Exception as e:
#             print(e)
#         else:
#             return response.json()
        
        
            