from typing import Dict, Tuple, Union

#if TYPE_CHECKING:
from aiohttp import ClientSession

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
    
    def parse_filters(self, base_endpoint: str, filter: dict):
        base_endpoint += "/?"
        list_filters = []

        for index, key in enumerate(filter):
            filters = f"filter[{key}]={filter.get(key)}" # Todo: enconding?

            if index >= 1:
                filters = "&" + filters
            
            list_filters.append(filters)

        for filter in list_filters:
            base_endpoint += filter
        
        return base_endpoint

    async def close(self) -> None:
        if self.__session:
            await self.__session.close()
    
    async def request(self, method: str, endpoint: str, kwargs=None, filters: dict = None, includes: list = None) -> Union[Tuple, Dict]:
        base_endpoint = self.url + endpoint

        if filters:
            base_endpoint = self.parse_filters(base_endpoint, filters)
        
        if includes:
            base_endpoint = base_endpoint + f"/?include={','.join(includes)}"
            
        async with self.__session.request(method, base_endpoint, json=kwargs) as response:
            response_json = await response.json()
            await self.close()

            return response.status, response_json















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
        
        
            