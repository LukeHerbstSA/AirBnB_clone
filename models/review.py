#!/usr/bin/python3
"""review file for review objs"""

from .base_model import BaseModel

class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
