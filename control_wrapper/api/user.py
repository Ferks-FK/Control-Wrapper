from typing import TYPE_CHECKING, Union, Dict, List

#if TYPE_CHECKING:
from .http import HTTPClient
from ..constants import *
from ..errors import MissingParameter, UnknownParameter, HTTPException, ExcessiveParametres

class User(HTTPClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def list_users(
        self,
        name: str = None,
        email: str = None,
        server_limit: int = None,
        pterodactyl_id: int = None,
        role: str = None,
        suspended: bool = None,
        includes: list = None
    ) -> Union[Dict, List[Dict], None]:
        """
        Returns all users registered in the system.

        Optionally you can provide user query filters.

        Filters
        -------
        name: :class:`str`
            The user name.
        email: :class:`str`
            The user email.
        server_limit: :class:`int`
            Limit of user servers.
        pterodactyl_id: :class:`int`
            The Pterodactyl ID of the user.
        role: :class:`str`
            The user role. Available Roles: `['admin', 'mod', 'client', 'member']`.
        suspended: :class:`bool`
            Whether the user is suspended or not.
        
        Includes
        --------
        includes: :class:`list`
            List of includes. Available Includes: `['servers', 'payments', 'vouchers', 'discordUser', 'notifications']`.

        Returns
        -------
        :class:`Union[Dict, List[Dict], None]`

        """

        filters = {
            'name': name,
            'email': email,
            'server_limit': server_limit,
            'pterodactyl_id': pterodactyl_id,
            'role': role,
            'suspended': 1 if suspended else (0 if suspended is False else suspended) # https://github.com/ControlPanel-gg/dashboard/issues/582
        }
        filters = {key: value for key, value in filters.items() if value is not None}

        if filters and includes:
            await self.close()
            raise ExcessiveParametres("You cannot use the 'filters' and 'includes' parameters together, just use one of them.")

        for include in includes:
            if include not in AVAILABLE_INCLUDES_USERS_PARAMS:
                await self.close()
                raise UnknownParameter(f"The include '{include}' is not recognized. Available Includes: {AVAILABLE_INCLUDES_USERS_PARAMS}.")

        response = await self.request("GET", "api/users", filters=filters, includes=includes)

        if not response[1]['data']:
            return None

        return response[1]
    
    async def user_details(self, id: int) -> Union[Dict, None]:
        response = await self.request("GET", f"api/users/{id}")

        if response[0] == 404:
            return None

        return response[1]
    
    async def update_user(self, id: int, **kwargs) -> Dict:
        for key in kwargs.keys():
            if key not in AVAILABLE_UPDATE_USER_PARAMS:
                await self.close()
                raise UnknownParameter(f"The parameter '{key}' is not recognized. Available Parameter: {AVAILABLE_UPDATE_USER_PARAMS}.")
            
        if kwargs.get('name') is None or kwargs.get('email') is None:
            await self.close()
            raise MissingParameter("You need to specify the parameters 'name' and 'email' for the user update.")
        
        if kwargs.get('role') is not None:
            if kwargs.get('role') not in AVAILABLE_UPDATE_ROLE_PARAMS:
                await self.close()
                raise UnknownParameter(f"The value '{kwargs.get('role')}' does not exist. Available Values: {AVAILABLE_UPDATE_ROLE_PARAMS}.")
        
        response = await self.request("PATCH", f"api/users/{id}", kwargs)
        return response[1]
    
    async def suspend_user(self, id: int) -> Dict:
        response = await self.request("PATCH", f"api/users/{id}/suspend")

        if response[0] == 422:
            raise HTTPException("This user is already suspended.")
        
        return response[1]
    
    async def unsuspend_user(self, id: int) -> Dict:
        response = await self.request("PATCH", f"api/users/{id}/unsuspend")
        
        if response[0] == 422:
            raise HTTPException("You cannot unsuspend a user who is not suspended.")
        
        return response[1]