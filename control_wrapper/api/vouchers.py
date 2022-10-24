from typing import Union, Dict, Any
from .http import HTTPClient
from ..utils import parse_dict
from ..errors import UnknownParameter
from ..constants import AVAILABLE_INCLUDES_VOUCHERS_PARAMS, AVAILABLE_UPDATE_VOUCHER_PARAMS
from datetime import datetime
from random import choices
from string import ascii_uppercase, digits

class Voucher(HTTPClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def list_vouchers(
        self,
        code: str = None,
        memo: str = None,
        credits: int = None,
        uses: int = None,
        includes: list = None
    ) -> Union[Dict, None]:
        """|Corrotine|

        Returns
        -------
        Returns all registered vouchers, or `None` if a specific voucher is not found.

        Optionally you can provide Filters and Includes for user query.

        Filters
        -------
        code: :class:`str`
            The voucher code.
        memo: :class:`str`
            The voucher memo.
        credits: :class:`int`
            The voucher credits.
        uses: :class:`int`
            The uses for voucher.

        Includes
        --------
        includes: :class:`list`
            List of includes. Available Includes: `['users', 'usersCount']`.
        """
        filters = {
            'code': code,
            'memo': memo,
            'credits': credits,
            'uses': uses
        }
        filters = parse_dict(filters)

        if includes:
            for include in includes:
                if include not in AVAILABLE_INCLUDES_VOUCHERS_PARAMS:
                    await self._close()
                    raise UnknownParameter(f"The include '{include}' is not recognized. Available Includes: {AVAILABLE_INCLUDES_VOUCHERS_PARAMS}.")

        response = await self._request("GET", "api/vouchers", filters=filters, includes=includes)

        if not response[1]['data']:
            return None
        
        return response[1]
    
    async def voucher_details(self, id: int, includes: list = None) -> Union[Dict, None]:
        """|Corrotine|

        Returns
        -------
        Returns data for a specific voucher, or `None` if not found.
        
        Includes
        --------
        includes: :class:`list`
            List of includes. Available Includes: `['users', 'usersCount']`.
        """
        if includes:
            for include in includes:
                if include not in AVAILABLE_INCLUDES_VOUCHERS_PARAMS:
                    await self._close()
                    raise UnknownParameter(f"The include '{include}' is not recognized. Available Includes: {AVAILABLE_INCLUDES_VOUCHERS_PARAMS}.")

        response = await self._request("GET", f"api/vouchers/{id}", includes=includes)

        if response[0] == 404:
            return None
        
        return response[1]
    
    async def update_voucher(
        self,
        id: int,
        code: str,
        uses: int,
        credits: int,
        **kwargs: Any
    ):
        """|Corrotine|

        Returns
        -------
        Returns a dict containing the updated voucher information, or an error if the voucher ID does not exist.
        
        Parameters
        ----------
        id: :class:`int`
            The voucher ID.
        code: :class:`str`
            The voucher code.
        uses: :class:`int`
            The uses for voucher.
        credits: :class:`int`
            The voucher credits.
        memo: Optional[:class:`str`]
            The voucher memo.
        expires_at: Optional[:class:`str` | :class:`datetime`]
            A `str` or `datetime` object containing the voucher expiration date.
        """
        for key, value in kwargs.items():
            if key not in AVAILABLE_UPDATE_VOUCHER_PARAMS:
                await self._close()
                raise UnknownParameter(f"The parameter '{value}' is not recognized. Available Parameters: {AVAILABLE_UPDATE_VOUCHER_PARAMS}.")

            if key == "expires_at" and isinstance(kwargs['expires_at'], datetime):
                kwargs['expires_at'] = kwargs['expires_at'].strftime("%d-%m-%Y")
        
        kwargs['code'] = code
        kwargs['uses'] = uses
        kwargs['credits'] = credits

        response = await self._request("PATCH", f"api/vouchers/{id}", kwargs)

        if response[0] == 422:
            return response[1]['errors']
        elif response[0] == 404:
            return response[1]['message']
        
        return response[1]
    
    async def create_voucher(self, uses: int, credits: int, code: str = None, **kwargs: Any):
        """|Corrotine|

        Returns
        -------
        Returns a dict with the information of the voucher created.

        If any of the supplied parameters are in the wrong format or are missing, an error will be returned.

        Parameters
        ----------
        uses: :class:`int`
            The number of times this voucher can be used.
        credits: :class:`int`
            The amount of credits the user will receive when using this voucher.
        code: Optional[:class:`str`]
            The voucher code. If none is provided, a random code will be generated.
        memo: Optional[:class:`str`]
            The voucher memo.
        expires_at: Optional[:class:`str` | :class:`datetime`]
            A `str` or `datetime` object containing the voucher expiration date.
        """
        if code is None:
            code = ''.join(choices(ascii_uppercase + digits, k=7)) # Generate a random 7-digit code.
        
        for key, value in kwargs.items():
            if key not in AVAILABLE_UPDATE_VOUCHER_PARAMS:
                await self._close()
                raise UnknownParameter(f"The parameter '{value}' is not recognized. Available Parameters: {AVAILABLE_UPDATE_VOUCHER_PARAMS}.")

            if key == "expires_at" and isinstance(kwargs['expires_at'], datetime):
                kwargs['expires_at'] = kwargs['expires_at'].strftime("%d-%m-%Y")
        
        kwargs['code'] = code
        kwargs['uses'] = uses
        kwargs['credits'] = credits

        response = await self._request("POST", "api/vouchers", kwargs)

        if response[0] == 422:
            return response[1]['errors']
        
        return response[1]
    
    async def delete_voucher(self, id: int):
        """|Corrotine|

        Returns
        -------
        Returns the deleted voucher information, or an error if the ID passed in does not exist.

        Parameters
        ----------
        id: :class:`int`
            The voucher ID.
        """
        response = await self._request("DELETE", f"api/vouchers/{id}")

        if response[0] == 404:
            return response[1]['message']

        return response[1]
