#!/usr/bin/env python3
""" SessionAuth inherits from Auth
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ implements SessionAuth authentication mechanism
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a session id for a user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        sessionID = str(uuid.uuid4())
        self.user_id_by_session_id[sessionID] = user_id
        return sessionID
