import base64
from itertools import cycle, izip


def xorencode(string, key="_"):
    """Return the base64 encoded XORed version of string. This is XORed with
    key which defaults to a single underscore."""
    return base64.encodestring(
        ''.join(
            chr(ord(c) ^ ord(k)) for c, k in izip(string, cycle(key)))).strip()


def xordecode(string, key="_"):
    """Returns the base64 decoded, XORed version of string. This is XORed with
    key, which defaults to a single underscore"""
    string = base64.decodestring(string)
    return ''.join(
        chr(ord(c) ^ ord(k)) for c, k in izip(string, cycle(key))).strip()
