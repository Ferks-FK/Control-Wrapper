from .api import *

class ControlWrapper:
    """
    The main class for connecting to the CPGG API.

    Parameters
    ----------
    url: :class:`str`
        The URL of your CPGG client.
    token: :str:`str`
        Your CPGG client token.
    """
    def __init__(self, url: str, token: str):
        if not url.endswith("/"):
            url += "/"

        self._url = url
        self._token = token

    @property
    def user(self):
        return User(self._token, self._url)
    
    @property
    def server(self):
        return Server(self._token, self._url)
    
    @property
    def voucher(self):
        return Voucher(self._token, self._url)
    
    @property
    def notification(self):
        return Notifications(self._token, self._url)