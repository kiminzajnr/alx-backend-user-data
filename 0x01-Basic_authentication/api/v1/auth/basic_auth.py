#!/usr/bin/env python3
""" Basic auth
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ returns the base64 part of the Authorization header
        for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header[0:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64.b64encode(base64.b64decode(
                base64_authorization_header)) == base64_authorization_header
        except BaseException:
            return None
        return base64.b64decode(
            base64_authorization_header + '===').decode('utf-8')
