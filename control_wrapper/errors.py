class ControlWrapperException(Exception):
    """Base exception class for Control-Wrapper.

    Used for any exception of this library.
    """
    pass

class MissingParameter(ControlWrapperException):
    """Exception generated when a parameter is missing."""
    pass

class MaxRetriesExeption(ControlWrapperException):
    """Exception generated when the maximum number of retries is reached."""
    pass