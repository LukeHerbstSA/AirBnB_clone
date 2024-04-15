#!/usr/bin/python3
"""Child of BaseModel, user objects."""
from .base_model import BaseModel

class User(BaseModel):
    """Class user that stores public attributes for each user."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
