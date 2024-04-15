#!/usr/bin/python3
"""Console experience provided by cmd to create/manipulate created objects."""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.base_model import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Provide a CLI to create and manipulate hbnb objects."""

    prompt = "(hbnb) "
    available_cls = ["BaseModel", "User", "State", "City", "Amenity"
            , "Place", "Review"]

    def scope_checker(self, arg):
        """Check if an objects class is within the scope."""
        flag = 1
        for item in self.available_cls:
            if (item in arg):
                flag = 0
        return (True if flag == 0 else False)

    def do_quit(self, arg):
        """Program exits on quit command passed."""
        return True

    def do_EOF(self, arg):
        """Program exits on EOF character passed in stdin."""
        return True

    def do_help(self, arg):
        """Use in conjunction with a corresponding desired cmd."""
        super().do_help(arg)

    def do_create(self, arg):
        """Create hbnb objects."""
        if (len(arg) == 0):
            print("** class name missing **")
        elif ((self.scope_checker)(arg)):
            for item in self.available_cls:
                if (arg == item):
                    obj = eval(item + "()")
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string repr of an instance."""
        argsplit = arg.split(" ")
        if (len(argsplit) == 0):
            print("** class name missing **")
        elif (not (self.scope_checker)(argsplit[0])):
            print("** class doesn't exist **")
        elif (len(argsplit) > 1):
            instances = storage._FileStorage__objects
            found = -1
            for key, value in instances.items():
                if (value.id in argsplit[1]):
                    print(value)
                    found = 0
            if (found == -1):
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Destroy instances of id and class."""
        argsplit = arg.split(" ")
        if (len(argsplit) == 0):
            print("** class name missing **")
        elif (not (self.scope_checker)(argsplit[0])):
            print("** class doesn't exist **")
        elif (len(argsplit) > 1):
            destroy = -1
            instances = storage._FileStorage__objects
            for key, value in instances.items():
                if (value.id in argsplit[1]):
                    key_name = key
                    destroy = 0
            if (destroy == 0):
                instances.pop(key_name)
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """Print all instances in file__objects."""
        objs = []
        for key, value in storage._FileStorage__objects.items():
            objs.append(value)
        if (len(arg) == 0):
            print("[", end="")
            for i in range(0, len(objs)):
                print("\"{}\"".format(objs[i]), end="")
                if (i != len(objs) - 1):
                    print(", ", end="")
            print("]")
        elif ((self.scope_checker)(arg)):
            print("[", end="")
            for i in range(0, len(objs)):
                if (type(objs[i]).__name__ == arg):
                    print("\"{}\"".format(objs[i]), end="")
                    if (i != len(objs) - 1):
                        print(", ", end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update passed object with passed attr name and val."""
        argsplit = arg.split(" ")
        id_check = -1
        instances = storage._FileStorage__objects
        if (len(argsplit) == 0):
            print("class name missing **")
        elif (len(argsplit) == 1):
            print("** instance id missing **")
        elif (len(argsplit) == 2):
            print("** attribute name missing **")
        elif (len(argsplit) == 3):
            print("** value missing **")
        else:
            if (not (self.scope_checker)(argsplit[0])):
                print("** class doesn't exist **")
            else:
                for key, value in instances.items():
                    if (key == "{}.{}".format(argsplit[0], argsplit[1])):
                        setattr(value, argsplit[2], argsplit[3])
                        id_check = 0
                if (id_check == -1):
                    print("** no instance found **")
                else:
                    storage.save()


if (__name__ == "__main__"):
    HBNBCommand().cmdloop()
