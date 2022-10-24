from typing import Union, Dict, List, Any
from .http import HTTPClient
from ..constants import *
from ..errors import UnknownParameter, MissingParameter, UnknownRole
from ..utils import parse_dict
from secrets import token_urlsafe

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
    ) -> Union[Dict, None]:
        """|Corrotine|

        Returns
        -------
        Returns all users registered in the system or `None` if a specific user is not found.

        Optionally you can provide Filters and Includes for user query.

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
            List of includes. Available Includes: `['servers', 'serversCount', 'notifications', 'notificationsCount', 'payments', 'paymentsCount', 'vouchers', 'vouchersCount', 'discordUser', 'discordUserCount']`.
        """

        filters = {
            'name': name,
            'email': email,
            'server_limit': server_limit,
            'pterodactyl_id': pterodactyl_id,
            'role': role,
            'suspended': 1 if suspended else (0 if suspended is False else suspended) # https://github.com/ControlPanel-gg/dashboard/issues/582
        }
        filters = parse_dict(filters)

        if includes:
            for include in includes:
                if include not in AVAILABLE_INCLUDES_USERS_PARAMS:
                    await self._close()
                    raise UnknownParameter(f"The include '{include}' is not recognized. Available Includes: {AVAILABLE_INCLUDES_USERS_PARAMS}.")

        response = await self._request("GET", "api/users", filters=filters, includes=includes)

        if not response[1]['data']:
            return None

        return response[1]
    
    async def user_details(self, id: int, includes: list = None) -> Union[Dict, None]:
        """|Corrotine|

        Returns
        -------
        Returns data for a specific user, or None if the user is not found.

        This is useful for checking whether a user has verified his discord account.

        Parameters
        ----------
        id: :class:`int`
            The user ID or discord_id.
        
        Includes
        --------
        includes: :class:`list`
            List of includes. Available Includes: `['servers', 'serversCount', 'notifications', 'notificationsCount', 'payments', 'paymentsCount', 'vouchers', 'vouchersCount', 'discordUser', 'discordUserCount']`.
        """
        if includes:
            for include in includes:
                if include not in AVAILABLE_INCLUDES_USERS_PARAMS:
                    await self._close()
                    raise UnknownParameter(f"The include '{include}' is not recognized. Available Includes: {AVAILABLE_INCLUDES_USERS_PARAMS}.")

        response = await self._request("GET", f"api/users/{id}", includes=includes)

        if response[0] == 404:
            return None

        return response[1]
    
    async def update_user(self, id: int, name: str, email: str, **kwargs: Any) -> Union[Dict, Dict[List, str]]:
        """|Corrotine|

        Returns
        -------
        Returns a dictionary with the user updated data.

        If the `email` is in the incorrect format, or the user ID passed in does not exist, an error is returned.
        
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
                await self._close()
                raise UnknownParameter(f"The parameter '{value}' is not recognized. Available Parameters: {AVAILABLE_UPDATE_USER_PARAMS}.")

            if key == "role" and value not in AVAILABLE_UPDATE_ROLE_PARAMS:
                await self._close()
                raise UnknownRole(f"The role '{value}' is not recognized, Available Roles: {AVAILABLE_UPDATE_ROLE_PARAMS}.")

        kwargs['name'] = name
        kwargs['email'] = email

        response = await self._request("PATCH", f"api/users/{id}", kwargs)

        if response[0] == 422:
            return response[1]['errors']
        elif response[0] == 404:
            return response[1]['message']

        return response[1]
    
    async def suspend_user(self, id: int) -> Union[Dict, Dict[List, str]]:
        """|Corrotine|

        Returns
        -------
        Returns a dict of the user who was suspended.

        If the user is already suspended, or, the user ID passed in does not exist, an error will be returned.

        Parameters
        ----------
        id: :class:`int`
            The user ID.
        """
        response = await self._request("PATCH", f"api/users/{id}/suspend")

        if response[0] == 422:
            return response[1]['errors']
        elif response[0] == 404:
            return response[1]['message']
        
        return response[1]
    
    async def unsuspend_user(self, id: int) -> Union[Dict, Dict[List, str]]:
        """|Corrotine|

        Returns
        -------
        Returns a dict of the user who had his suspension revoked.
        
        If the user is not already suspended, or, the user ID passed in does not exist, an error will be returned.

        Parameters
        ----------
        id: :class:`int`
            The user ID.
        """
        response = await self._request("PATCH", f"api/users/{id}/unsuspend")
        
        if response[0] == 422:
            return response[1]['errors']
        elif response[0] == 404:
            return response[1]['message']
        
        return response[1]
    
    async def increment_user(self, id: int, credits: int = None, server_limit: int = None) -> Union[Dict, Dict[List, str]]:
        """|Corrotine|

        Returns
        -------
        Returns a dict of the user who had an increment added.

        If the user ID passed in does not exist, or if any parameter has an incorrect value, an error will be returned.

        Parameters
        ----------
        id: :class:`int`
            The user ID.
        credits: :class:`int`
            The amount of credits that will be added to the user.
        server_limit: :class:`int`
            The amount of server limit that will be added to the user.
        
        Info
        ----
        This method will not overwrite the user's existing server credits or limits, instead the new value will be added to the old one.
        
        The `credits` and `server_limit` parameters are not required simultaneously, but one of them must be supplied.
        """
        if credits is None and server_limit is None:
            await self._close()
            raise MissingParameter("The parameters 'credits' and 'server_limit' is required, that is missing.")
        
        kwargs = {
            'credits': credits,
            'server_limit': server_limit
        }

        if kwargs['credits'] is None:
            kwargs.pop('credits')
        
        if kwargs['server_limit'] is None:
            kwargs.pop('server_limit')

        response = await self._request("PATCH", f"api/users/{id}/increment", kwargs)

        if response[0] == 422:
            return response[1]['errors']
        elif response[0] == 404:
            return response[1]['message']
        
        return response[1]
    
    async def decrement_user(self, id: int, credits: int = None, server_limit: int = None) -> Union[Dict, Dict[List, str]]:
        """|Corrotine|

        Returns
        -------
        Returns a dict of the user who had an decrement added.

        If the user ID passed in does not exist, or if any parameter has an incorrect value, an error will be returned.

        Parameters
        ----------
        id: :class:`int`
            The user ID.
        credits: :class:`int`
            The amount of credits that will be removed from the user.
        server_limit: :class:`int`
            The amount of server limit that will be removed from the user.
        
        Info
        ----
        This method will not overwrite the user's existing server credits or limits, instead the new value will be deducted from the old one.
        
        The `credits` and `server_limit` parameters are not required simultaneously, but one of them must be supplied.
        """
        if credits is None and server_limit is None:
            await self._close()
            raise MissingParameter("The parameters 'credits' and 'server_limit' is required, that is missing.")
        
        kwargs = {
            'credits': credits,
            'server_limit': server_limit
        }

        if kwargs['credits'] is None:
            kwargs.pop('credits')
        
        if kwargs['server_limit'] is None:
            kwargs.pop('server_limit')

        response = await self._request("PATCH", f"api/users/{id}/decrement", kwargs)

        if response[0] == 422:
            return response[1]['errors']
        elif response[0] == 404:
            return response[1]['message']
        
        return response[1]
    
    async def create_user(self, name: str, email: str, password: str = None) -> Union[Dict, Dict[List, str]]:
        """|Corrotine|
        
        Returns
        -------
        Returns a dict of the new registered user.

        If any of the supplied parameters are in the wrong format or are missing, (with the exception of the password), an error will be returned.
        
        Parameters
        ----------
        name: :class:`str`
            This parameter must be in the format alpha_num and be at least 4 to 30 characters long.
        email: :class:`str`
            This parameter must be in the correct format and be unique.
        password: Optional[:class:`str`]
            This parameter must be 8 to 191 characters long. If a password is not supplied, a random one will be generated.
        
        Info
        ----
        If a random password is generated, this method or the API will NOT return the password.
        In this case, the user will need to reset their password on the website.
        """
        if password is None:
            password = token_urlsafe(24)
        
        kwargs = {
            'name': name,
            'email': email,
            'password': password
        }

        response = await self._request("POST", "api/users", kwargs)

        if response[0] == 422:
            return response[1]['errors']

        return response[1]
    
    async def delete_user(self, id: int) -> Dict:
        """|Corrotine|

        Returns
        -------
        Returns a dict of the user that was deleted.

        If the user ID does not exist, an error is returned.
        
        Parameters
        ----------
        id: :class:`int`
            The user ID.
        
        Info
        ----
        Currently this endpoint will delete the user, even if they have servers associated with them, so use this with caution.
        """
        response = await self._request("DELETE", f"api/users/{id}")

        if response[0] == 404:
            return response[1]['message']
        
        return response[1]
    


