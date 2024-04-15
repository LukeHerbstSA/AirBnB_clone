#!/usr/bin/python3
"""BaseModel classes to store basic objects."""

from . import storage
from datetime import datetime
import uuid


class BaseModel:
    """Class base model defines basic objs to be used."""

    def __str__(self):
        """Print the string repr of an instance."""
        id_and_dict = "({}) {}".format(self.id, self.__dict__)
        str_rep = "[{}] ".format(type(self).__name__) + id_and_dict
        return (str_rep)

    def __init__(self, *args, **kwargs):
        """Initialize an instance of the class (or child class user)."""
        if (kwargs):
            for key, value in kwargs.items():
                if (key != "__class__"):
                    if (key == "updated_at" or key == "created_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Save inst of BaseModel using file storage inst."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Construct an expanded dictionary to return."""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = type(self).__name__
        inst_dict["created_at"] = (self.created_at).isoformat()
        inst_dict["updated_at"] = (self.updated_at).isoformat()
        return (inst_dict)
