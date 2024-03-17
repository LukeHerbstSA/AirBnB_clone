#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
bm1 = BaseModel()
print(bm1)
print(storage._FileStorage__file_path)
print(storage._FileStorage__objects)
bm1.save()
