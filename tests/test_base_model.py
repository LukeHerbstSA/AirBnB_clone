#!/usr/bin/python3
"unittests testing if base_model works"

import unittest

from ..models.__init__ import storage
from ..models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """class to test functionalites of test_base_model"""
    def test___str__(self):
        """tests return of __str__ method by looking for dict"""
        bm = BaseModel()
        self.assertEqual(type(bm.__str__), str)

    def test___init__(self):
        """test initialization of instances of base model"""
        bm1 = BaseModel()
        self.assertEqual(type(bm1).__name__, "BaseModel")
        self.assertEqual(type(bm1.updated_at), str)
        self.assertEqual(type(bm1.created_at), str)
        self.assertEqual(type(bm1.id), str)

    def test_save(self):
        """tests saving of instances"""
        bm1 = BaseModel()
        bm1.save()
        instances = storage.__objects
        dict_key = "{}{}".format("BaseModel", bm1.id)
        self.assertEqual((instances[dict_key]).id, bm1.id)

    def test_to_dict(self):
        """tests dict repr of returned dict of instance"""
        bm1 = BaseModel()
        dictionary_inst = bm1.to_dict()
        self.assertEqual(type(dictionary_inst), dict)

if (__name__ == "__main__"):
    unittest.main()
