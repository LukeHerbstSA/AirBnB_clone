#!/usr/bin/python3
"""BaseModel classes to store basic objects"""

from __init__ import storage
from datetime import datetime
import uuid

class BaseModel:
    """class base model defines basic objs to be used"""
    def __str__(self):
        """prints the string repr of an instance"""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def __init__(self, *args, **kwargs):
        """initializes an instance of the class (or child class user)"""
        if (kwargs is not None):
            for key, value in kwargs.items():
                if (key != "__class__"):
                    if (key == "updated_at" or key == "created_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime
            self.updated_at = datetime.datetime
            storage.new(self)

    def save(self):
        """saves inst of BaseModel using file storage inst"""
        self.updated_at = datetime.datetime
        storage.save(self)

    def to_dict(self):
        """constructs an expanded dictionary inst to return to terminal caller"""
        inst_dict = self.__dict__
        inst_dict["__class__"] = type(self).__name__
        inst_dict["created_at"] = (self.created_at).isoformat()
        inst_dict["updated_at"] = (self.updated_at).isoformat()
        return (inst_dict)
