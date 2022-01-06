#!/usr/bin/env python3
"""
Encrypting password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a hashed password"""
    hashed = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
    return hashed
