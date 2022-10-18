from typing import TYPE_CHECKING, Union, Dict, List

#if TYPE_CHECKING:
from .http import HTTPClient
from ..constants import UPDATE_USER_PARAMS
from ..errors import MissingParameter, UnknownParameter

class User(HTTPClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def list_users(self) -> Union[Dict, List[Dict]]:
        return await self.request("GET", "api/users")
    
    async def user_details(self, id: int) -> Union[Dict, None]:
        return await self.request("GET", f"api/users/{id}")
    
    async def update_user(self, id: int, **kwargs):
        print(kwargs)
        if not kwargs:
            await self.close()
            raise MissingParameter(f"You need to specify at least one user parameter to be updated. Available Parameters: {UPDATE_USER_PARAMS}.")
        
        for key in kwargs.keys():
            if key not in UPDATE_USER_PARAMS:
                await self.close()
                raise UnknownParameter(f"The parameter {key} is not recognized.")

        return await self.request("PATCH", f"api/users/{id}", kwargs)