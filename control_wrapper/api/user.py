from typing import TYPE_CHECKING, Union, Dict, List

#if TYPE_CHECKING:
from .http import HTTPClient

class User(HTTPClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def list_users(self) -> Union[Dict, List[Dict]]:
        return await self._make_request("api/users")
    
    async def user_details(self, id: int) -> Union[Dict, None]:
        return await self._make_request("api/users/{id}", id)