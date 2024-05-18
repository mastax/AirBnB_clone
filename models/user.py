#!/usr/bin/python3
"""This File Contain The Class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class That Inherits From BaseModel Class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""