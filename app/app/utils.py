"""Application utils module."""

from hashlib import md5
from base64 import urlsafe_b64encode


def generate_code(url: str, start: int = 0, length: int = 8) -> str:
    """
    This function is responsible for generating code between defined two indexes.
    """
    return urlsafe_b64encode(md5(url.encode('utf-8')).hexdigest().encode('utf-8')).decode('utf-8')[start:start+length]
