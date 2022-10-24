from typing import Dict, Tuple, Union
from aiohttp import ClientSession, ClientTimeout
from urllib import parse

class HTTPClient:
    def __init__(self, token: str, url: str) -> None:
        self.__token = token
        self.__url = url
        headers: Dict[str, str] = {
            "Authorization": "Bearer " + self.__token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.__timeout = ClientTimeout(total=2.5)
        self.__session: ClientSession = ClientSession(headers=headers, timeout=self.__timeout)
    
    def __parse_data(self, base_endpoint: str, filters: dict, includes: list) -> str:
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

    async def _close(self) -> None:
        if self.__session:
            await self.__session.close()
    
    async def _request(self, method: str, endpoint: str, kwargs=None, filters: dict = None, includes: list = None) -> Union[Tuple, Dict]:
        base_endpoint = self.__parse_data(self.__url + endpoint, filters, includes)
  
        async with self.__session.request(method, base_endpoint, json=kwargs) as response:
            response_json = await response.json()
            await self._close()

            return response.status, response_json
            