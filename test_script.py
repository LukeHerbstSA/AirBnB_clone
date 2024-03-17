#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
bm1 = BaseModel()
print(bm1)
print(storage._FileStorage__file_path)
print(storage._FileStorage__objects)
bm1.save()
print("done testing basic features --")
bm2 = {"id": "6728496b-1902-4005-a805-358361a66bc7", "created_at": "2024-03-17T19:55:18.022612", "updated_at": "2024-03-17T19:55:18.022676", "__class__": "BaseModel"}
print("dict: {}".format(bm2))
bm2 = BaseModel(**(bm2))
print(bm2)
