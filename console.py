#!/usr/bin/python3
"""console experience provided by cmd to create/manipulate created objects"""

import cmd
import sys
from models.user import User
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """provides a CLI to create and manipulate hbnb objects"""
    prompt = "(hbnb)"

    def scope_checker(self, arg):
        """checks if an objects class is within the scope"""
        available_cls = ["BaseModel", "User"]
        if (arg in available_cls):
            return True
        else:
            return False

    def do_quit(self, arg):
        """program exits on quit command passed"""
        return True

    def do_EOF(self, arg):
        """program exits on EOF character passed in stdin"""
        return True

    def do_help(self, arg):
        """used in conjunction with a corresponding desired cmd"""
        super().do_help(arg)

    def do_create(self, arg):
        """creates hbnb objects"""
        if (len(arg) == 1):
            print("** class name missing **")
        elif ((self.scope_checker)(arg[1])):
            if (arg[1] == "BaseModel"):
                obj = BaseModel()
            if (arg[1] == "User"):
                obj = User()
            print(obj.id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints the string repr of an instance"""
        if (len(arg) == 1):
            print("** class name missing **")
        if (len(arg) == 2):
            print("** instance id missing **")
        if (not (self.scope_checker)(arg[1])):
            print("** class doesn't exist **")
        instances = storage.__objects
        found = -1
        for key, value in instances.items():
            if (arg[2] in key):
                print(value.__dict__)
                found = 0
        if (found == -1):
            print("** no instance found **")

    def do_destroy(self, arg):
        """destroys instances of id and class"""
        if (len(arg) == 1):
            print("** class name missing **")
        if (len(arg) == 2):
            print("** instance id missing **")
        if (not (self.scope_checker)(arg[1])):
            print("** class doesn't exist **")
        destroy = -1
        instances = storage.__objects
        for key, value in instances.items():
            if (key == "{}.{}".format(arg[1], arg[2])):
                instances.pop(key)
                destroy = 0
        if (destroy == 0):
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """prints all instances in file__objects"""
        instances = storage.__objects
        if (len(arg) == 1):
            for key, value in instances.items():
                print("{}".format(value.__dict__))
        elif (not (self.scope_checker)(arg[1])):
            print("** class doesn't exist **")
        else:
            for key, value in instances.items():
                if (arg[1] == type(value).__name__):
                    print("{}".format(value.__dict__))

    def do_update(self, arg):
        """updates passed object with passed attr name and val"""
        id_check = -1
        instances = storage.__objects
        if (len(arg) == 1):
            print("class name missing **")
        elif (len(arg) == 2):
            print("** instance id missing **")
        elif (len(arg) == 3):
            print("** attribute name missing **")
        elif (len(arg) == 4):
            print("** value missing **")
        else:
            if (not (self.scope_checker)(arg[1])):
                print("** class doesn't exist **")
            else:
                for key, value in instances.items():
                    if (key == "{}.{}".format(arg[1], arg[2])):
                        setattr(value, arg[3], arg[4])
                        id_check = 0
            if (id_check == -1):
                print("** no instance found **")
            else:
                storage.save()


if (__name__ == "__main__"):
    HBNBCommand().cmdloop()
