from typing import Dict, Tuple, Union

#if TYPE_CHECKING:
from aiohttp import ClientSession
from urllib import parse

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
    
    def parse_data(self, base_endpoint: str, filters: dict, includes: list) -> str:
        base_endpoint += "?"

        if filters and includes:
            filters_includes = [{
                'filters': {f'filter[{filter}]': filters[filter] for filter in filters},
                'includes': ','.join(includes)
            }]
            return base_endpoint + parse.urlencode(filters_includes[0]['filters']) + f"&include={filters_includes[0]['includes']}"
        
        elif filters:
            filters = {
                'filters': {f'filter[{filter}]': filters[filter] for filter in filters}
            }
            return base_endpoint + parse.urlencode(filters['filters'])
        
        elif includes:
            return base_endpoint + f"&include={','.join(includes)}"

        return base_endpoint

    async def close(self) -> None:
        if self.__session:
            await self.__session.close()
    
    async def request(self, method: str, endpoint: str, kwargs=None, filters: dict = None, includes: list = None) -> Union[Tuple, Dict]:
        base_endpoint = self.parse_data(self.url + endpoint, filters, includes)
  
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
        
        
            