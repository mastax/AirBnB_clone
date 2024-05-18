#!/usr/bin/python3
"""This File Contain The Class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class That Inherits From BaseModel Class
    """
    place_id = ""
    user_id = ""
    text = ""