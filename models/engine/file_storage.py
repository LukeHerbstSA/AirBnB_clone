#!/usr/bin/python3
"""file storage class to store and reload created objects"""

import sys
import json
import os

class FileStorage:
    """FileStorage instance that writes and reads from .json file"""
    __file_path = "{}/file.json".format(os.path.dirname(os.path.abspath(__file__)))
    __objects = {}

    def all(self):
        """returns all objects stored in __objects"""
        return (self.__objects)

    def new(self, obj):
        """adds passed objects to stored objects for later use"""
        keyname = "{}.{}".format(type(obj).__name__, obj.id)
        (self.__objects)[keyname] = obj
        self.save()

    def save(self):
        """overwrites storage file with objects in attr"""
        objs = (self.__objects).copy()
        for name_id, obj in objs.items():
            obj_dict = obj.to_dict()
            objs[name_id] = obj_dict
        json_dict = json.dumps(objs)
        try:
            with open(self.__file_path, "w+") as myfile:
                myfile.write(json_dict)
        except FileNotFoundError:
            pass

    def reload(self):
        """loads all objects stored in .json file into objects cls attr"""
        inst_dict = {}
        try:
            with open(self.__file_path, "r+") as myfile:
                json_dicts = myfile.read()
        except FileNotFoundError:
            return
        dict_instances = json.loads(json_dicts)
        for obj_name, obj_val in dict_instances.items():
            if ("BaseModel" in obj_name):
                from ..base_model import BaseModel
                obj_val = BaseModel(**(obj_val))
            if ("User" in obj_name):
                from ..user import User
                obj_val = User(**(obj_val))
            inst_dict[obj_name] = obj_val
        self.__objects = inst_dict
