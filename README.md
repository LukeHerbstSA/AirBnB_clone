This project is meant to make a clone of the AIRBNB software

It consists of a console file, that which will be used to add and manipulate objects of various available class
The BaseModel class is responsible for creating the framework of the system i.e: saving objects, retrieving info from a file storage instance, passing it to console
The FileStorage class is responsible for writing and retrieving objects to and from a .json file. This ensures objects are saved and reloaded when necessary

Usage to start:

./console.py

Usage to do perform various commands:

create BaseModel - this will create a new BaseModel instance complete with attributes

show BaseModel 1545rgresdf4 - an example of how one would display a particular instance - id's in the 3rd argument will differ from this example

all BaseModel - will display all instances of the BaseModel instance type

quit - quits console
