from typing import Union, Dict 
from .http import HTTPClient
from ..constants import AVAILABLE_NOTIFICATIONS_PARAMS
from ..errors import UnknownParamValue, HTTPException

class Notifications(HTTPClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def user_notifications(self, id: int) -> Union[Dict, None]:
        """|Corrotine|

        Returns
        -------
        Returns all notifications from the user, or `None` if user has no messages.
        
        If the user ID does not exist, an error is returned.

        Parameters
        ----------
        id: :class:`int`
            The user ID.
        """
        response = await self._request("GET", f"api/notifications/{id}")

        if response[0] == 404:
            return response[1]['message']
        
        if response[0] == 200 and not response[1]['data']:
            return None
        
        return response[1]
    
    async def notification_details(self, id: int, notification_id: str) -> Dict:
        """|Corrotine|

        Returns
        -------
        Returns a dict containing the notification information, or an error if the user ID or notification ID does not exist.
        
        Parameters
        ----------
        id: :class:`int`
            The user ID.
        notification_id: :class:`str`
            The notification ID.
        """
        response = await self._request("GET", f"api/notifications/{id}/{notification_id}")

        if response[0] == 404:
            return response[1]['message']
        
        return response[1]
    
    async def send_notification_to_all_users(self, title: str, content: str, via: str) -> Dict:
        """|Corrotine|

        Returns
        -------
        Returns a dict containing the sent message informations.

        Parameters
        ----------
        title: :class:`str`
            The title of the message.
        content: :class:`str`
            The content of the message.
        via: :class:`str`
            The way in which users will receive the message. Available Methods: `['mail', 'database']`.
        """
        if via not in AVAILABLE_NOTIFICATIONS_PARAMS:
            await self._close()
            raise UnknownParamValue(f"The value '{via}' of the parameter 'via' It is not recognized. Available Values: {AVAILABLE_NOTIFICATIONS_PARAMS}.")

        kwargs = {
            "title": title,
            "content": content,
            "via": via,
            "all": 1 # The method is to send to everyone, but why a parameter to decide if it is for everyone or not? lmao
        }

        response = await self._request("POST", "api/notifications", kwargs)
        
        if response[0] == 422:
            return response[1]['errors']
        
        if via == "mail" and response[0] == 500:
            raise HTTPException("An unexpected error occurred while sending the notification via 'mail', usually this happens when your SMTP server is not working properly.")

        return response[1]
    
    async def send_notification_to_specific_users(self, title: str, content: str, users: list, via: str) -> Dict:
        """|Corrotine|
        
        Returns
        -------
        Returns a dict containing the sent message informations.

        Parameters
        ----------
        title: :class:`str`
            The title of the message.
        content: :class:`str`
            The content of the message.
        users: :class:`list`
            The user ID's that will receive this message.
        via: :class:`str`
            The way in which users will receive the message. Available Methods: `['mail', 'database']`.
        """
        if via not in AVAILABLE_NOTIFICATIONS_PARAMS:
            await self._close()
            raise UnknownParamValue(f"The value '{via}' of the parameter 'via' It is not recognized. Available Values: {AVAILABLE_NOTIFICATIONS_PARAMS}.")
        
        users = [str(user) if isinstance(user, int) else user for user in users] # Convert all integers to string.

        kwargs = {
            "title": title,
            "content": content,
            "via": via,
            "users": ','.join(users) # Must be a comma-separated ID string. Why not just a list/array? :/
        }

        response = await self._request("POST", "api/notifications", kwargs)

        if response[0] == 422:
            return response[1]['errors']

        if via == "mail" and response[0] == 500:
            raise HTTPException("An unexpected error occurred while sending the notification via 'mail', usually this happens when your SMTP server is not working properly.")

        return response[1]
    
    async def delete_all_notifications(self, id: int) -> Dict:
        """|Corrotine|
        
        Returns
        -------
        Returns a dict containing the information of the deleted messages.

        Parameters
        ----------
        id: :class:`int`
            The user ID.

        Info
        ----
        This method deletes ALL messages from a specific user.
        """
        response = await self._request("DELETE", f"api/notifications/{id}")

        if response[0] == 404:
            return response[1]['message']
        
        return response[1]
    
    async def delete_notification(self, id: int, notification_id: str) -> Dict:
        """|Corrotine|
        
        Returns
        -------
        Returns a dict containing the information of the deleted messages.

        Parameters
        ----------
        id: :class:`int`
            The user ID.
        notification_id: :class:`str`
            The notification ID.
        
        Info
        ----
        This method deletes only a specific message from a specific user.
        """
        response = await self._request("DELETE", f"api/notifications/{id}/{notification_id}")

        if response[0] == 404:
            return response[1]['message']
        
        return response[1]