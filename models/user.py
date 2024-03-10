#!/usr/bin/python3
"""child of BaseModel, user objects"""
from base_model import BaseModel


class User(BaseModel):
    """class user that stores public attributes for each user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
