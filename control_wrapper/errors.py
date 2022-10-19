class ControlWrapperException(Exception):
    """Base exception class for Control-Wrapper.

    Used for any exception of this library.
    """
    pass

class MissingParameter(ControlWrapperException):
    """Exception generated when a parameter is missing."""
    pass

class UnknownParameter(ControlWrapperException):
    """Exception generated when a parameter is not recognized."""
    pass

class MaxRetriesExeption(ControlWrapperException):
    """Exception generated when the maximum number of retries is reached."""
    pass

class HTTPException(ControlWrapperException):
    """Exception generated when HTTT request error occurs."""
    pass

class ExcessiveParametres(ControlWrapperException):
    """Exception generated when two or more incompatible parameters are passed."""
    pass