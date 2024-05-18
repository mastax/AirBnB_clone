#!/usr/bin/python3
"""This File Contain The Class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class That Inherits From BaseModel Class
    """
    state_id = ""
    name = ""