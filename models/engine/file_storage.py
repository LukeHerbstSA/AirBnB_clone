#!/usr/bin/python3
"""file storage class to store and reload created objects"""

import sys
import json
import uuid


class FileStorage:
    """FileStorage instance that writes and reads from .json file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objects stored in __objects"""
        return (self.__objects)

    def new(self, obj):
        """adds passed objects to stored objects for later use"""
        keyname = "{}.{}".format(type(obj).__name__, obj.id)
        (self.__objects)[keyname] = obj

    def save(self):
        """overwrites storage file with objects in attr"""
        json_dict = json.dumps(self.__objects)
        try:
            with open(self.__file_path, "w") as myfile:
                myfile.write(json_dict)
        except FileNotFoundError:
            pass

    def reload(self):
        """loads all objects stored in .json file into objects attr"""
        try:
            with open(self.__file_path, "r") as myfile:
                json_dicts = myfile.read()
            dict_instances = json.loads(json_dicts)
            self.__objects = dict_instances
        except FileNotFoundError:
            pass
