from typing import Union, Dict, Any
from .http import HTTPClient
from ..constants import AVAILABLE_INCLUDES_SERVERS_PARAMS
from ..errors import UnknownParameter
from datetime import datetime

class Server(HTTPClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def list_servers(
        self,
        name: str = None,
        identifier: str = None,
        user_id: int = None,
        pterodactyl_id: int = None,
        product_id: str = None,
        suspended: str | datetime = None,
        includes: list = None
    ) -> Union[Dict, None]:
        """|Corrotine|

        Returns
        -------
        Returns a dict containing all registered servers, or `None` if a specific server is not found.
        
        Optionally you can provide Filters and Includes for server query.

        Filters
        -------
        name: :class:`str`
            The server name.
        identifier: :class:`str`
            The server identifier.
        user_id: :class:`int`
            The user ID that owns the server.
        pterodactyl_id: :class:`int`
            The Pterodactyl ID of the user who owns the server.
        product_id: :class:`str`
            The ID of the product from which the server originates.
        suspended: :class:`str` | :class:`datetime`
            A `String` or `DateTime` object containing the date on which the server was suspended.

        Includes
        --------
        includes: :class:`list`
            List of includes. Available Includes: `['product', 'user'].`
        """
        filters = {
            'name': name,
            'identifier': identifier,
            'user_id': user_id,
            'pterodactyl_id': pterodactyl_id,
            'product_id': product_id,
            'suspended': suspended
        }
        filters = {key: value for key, value in filters.items() if value is not None}

        if filters.get('suspended') is not None and isinstance(filters['suspended'], datetime):
            filters['suspended'] = filters['suspended'].strftime("%Y-%m-%d")

        if includes:
            for include in includes:
                if include not in AVAILABLE_INCLUDES_SERVERS_PARAMS:
                    self.__close()
                    raise UnknownParameter(f"The include '{include}' is not recognized. Available Includes: {AVAILABLE_INCLUDES_SERVERS_PARAMS}.")

        response = await self._request("GET", "api/servers", filters=filters, includes=includes)

        if not response[1]['data']:
            return None
        
        return response[1]
    
    async def server_details(self, id: str) -> Union[Dict, None]:
        """|Corrotine|

        Returns
        -------
        Returns a dict containing the server information, or `None` if not found.

        Parameters
        ----------
        id: :class:`str`
            The server ID.
        """
        response = await self._request("GET", f"api/servers/{id}")

        if response[0] == 404:
            return None
        
        return response[1]
    
    async def suspend_server(self, id: str) -> Dict[str, Any]:
        """|Corrotine|

        Returns
        -------
        Returns a dict with the suspended server information, or an error if the ID does not exist.

        Parameters
        ----------
        id: :class:`str`
            The server ID.
        """
        response = await self._request("PATCH", f"api/servers/{id}/suspend")

        if response[0] == 404:
            return response[1]['message']
        
        return response[1]
    
    async def unsuspend_server(self, id: str) -> Dict[str, Any]:
        """|Corrotine|

        Returns
        -------
        Returns a dict with the information of the server that had its suspension revoked, or an error if the ID does not exist.

        Parameters
        ----------
        id: :class:`str`
            The server ID.
        """
        response = await self._request("PATCH", f"api/servers/{id}/unsuspend")

        if response[0] == 404:
            return response[1]['message']
        
        return response[1]
    
    async def delete_server(self, id: str) -> Dict[str, Any]:
        """|Corrotine|

        Returns
        -------
        Returns a dict containing the deleted server information, or an error if the ID does not exist.

        Parameters
        ----------
        id: :class:`str`
            The server ID.
        """
        response = await self._request("DELETE", f"api/servers/{id}")

        if response[0] == 404:
            return response[1]['message']
        
        return response[1]
