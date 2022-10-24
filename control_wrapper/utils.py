from typing import Dict

def parse_dict(dict: dict) -> Dict:
    """
    Returns
    -------
    This gets a dict, and returns the same dict, but without the keys that had their values as `None`.

    Parameters
    ----------
    dict: :class:`dict`
        The dict.
    """
    return {key: value for key, value in dict.items() if value is not None}