from typing import TYPE_CHECKING, Union, Dict, List, Any

#if TYPE_CHECKING:
from .http import HTTPClient
from ..constants import *
from ..errors import UnknownParameter, UnknownRole

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
        """|Corrotine|

        Returns
        -------

        Returns all users registered in the system or None if a specific user is not found.

        Optionally you can provide Filters or Includes user query.

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

        if includes:
            for include in includes:
                if include not in AVAILABLE_INCLUDES_USERS_PARAMS:
                    await self.__close()
                    raise UnknownParameter(f"The include '{include}' is not recognized. Available Includes: {AVAILABLE_INCLUDES_USERS_PARAMS}.")

        response = await self._request("GET", "api/users", filters=filters, includes=includes)

        if not response[1]['data']:
            return None

        return response[1]
    
    async def user_details(self, id: int) -> Union[Dict, None]:
        """|Corrotine|

        Returns
        -------
        Returns data for a specific user, or None if the user is not found.

        This is useful for checking whether a user has verified his discord account.

        Parameters
        ----------
        id: :class:`int`
            The user ID or discord_id.
        """
        response = await self._request("GET", f"api/users/{id}")

        if response[0] == 404:
            return None

        return response[1]
    
    async def update_user(self, id: int, name: str, email: str, **kwargs: Any) -> Union[Dict, Dict[List, str]]:
        """|Corrotine|

        Returns
        -------
        Returns a dictionary with the user updated data.

        If the `email` is in the incorrect format, an error will be returned.
        
        Parameters
        ----------
        id: :class:`int`
            The user ID.
        name: :class:`str`
            The new user name.
        email: :class:`str`
            The new email of the user.
        credits: Optional[:class:`int`]
            The new user credits.
        server_limit: Optional[:class:`int`]
            The amount of servers user can manage.
        role: Optional[:class:`str`]
            The new user role. Valid Roles: `['admin', 'mod', 'client', 'member']`.
        
        Info
        ----
        For some reason the API forces you to pass the user `name` and `email` address in order to update it.
        """
        for key, value in kwargs.items():
            if key not in AVAILABLE_UPDATE_USER_PARAMS:
                await self.__close()
                raise UnknownParameter(f"The parameter '{value}' is not recognized. Available Parameters: {AVAILABLE_UPDATE_USER_PARAMS}.")

            if key == "role" and value not in AVAILABLE_UPDATE_ROLE_PARAMS:
                await self.__close()
                raise UnknownRole(f"The role '{value}' is not recognized, Available Roles: {AVAILABLE_UPDATE_ROLE_PARAMS}.")

        kwargs['name'] = name
        kwargs['email'] = email

        response = await self._request("PATCH", f"api/users/{id}", kwargs)

        if response[0] == 422:
            return response[1]['errors']

        return response[1]
    
    async def suspend_user(self, id: int) -> Union[Dict, Dict[List, str]]:
        """|Corrotine|

        Returns
        -------
        Returns a dict of the user who was suspended.

        If the user is already suspended, an error will be returned.

        Parameters
        ----------
        id: :class:`int`
            The user ID.
        """
        response = await self._request("PATCH", f"api/users/{id}/suspend")

        if response[0] == 422:
            return response[1]['errors']
        
        return response[1]
    
    async def unsuspend_user(self, id: int) -> Union[Dict, Dict[List, str]]:
        """|Corrotine|

        Returns
        -------
        Returns a dict of the user who had his suspension revoked.
        
        If the user is not already suspended, an error will be returned.

        Parameters
        ----------
        id: :class:`int`
            The user ID.
        """
        response = await self._request("PATCH", f"api/users/{id}/unsuspend")
        
        if response[0] == 422:
            return response[1]['errors']
        
        return response[1]