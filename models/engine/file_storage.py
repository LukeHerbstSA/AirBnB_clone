#!/usr/bin/python3
"""file storage class to store and reload created objects"""

import sys
import json
import os

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
        current_data = (self.__objects).copy()
        objs = (self.__objects).copy()
        for name_id, obj in objs.items():
            obj_dict = obj.to_dict()
            objs[name_id] = obj_dict
        json_dict = json.dumps(objs)
        try:
            with open(self.__file_path, "w") as myfile:
                myfile.write(json_dict)
        except FileNotFoundError:
            pass
        self.__objects = current_data


    def reload(self):
        """loads all objects stored in .json file into objects attr"""
        try:
            with open(self.__file_path, "r") as myfile:
                json_dicts = myfile.read()
            dict_instances = json.loads(json_dicts)
            for obj_name, obj_val in dict_instances.items():
                if ("BaseModel" in obj_name):
                    from ..base_model import BaseModel
                    obj_val = BaseModel(**(obj_val))
                if ("User" in obj_name):
                    from ..user import User
                    obj_val = User(**(obj_val))
                dict_instances[obj_name] = obj_val
            self.__objects = dict_instances
        except FileNotFoundError:
            pass
