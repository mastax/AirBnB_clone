#!/usr/bin/python3
"""This module contain the HBNB console"""

import cmd
import json
import models
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter HBNB"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Place", "State\
", "City", "Amenity", "Review"]

    def do_quit(self, args):
        """Quit Command To Exit The Console"""
        return True

    def do_EOF(self, args):
        """EOF Command To Exit The Console"""
        return True

    def emptyline(self):
        """Perform Nothing When There's No Commmand Passed To The Console"""
        pass

    def do_create(self, args):
        """Creates a New Class Instance, Save In JSON File And Print The Id\n
        USAGE: (hbnb) create <class_name>"""
        if args == "":
            print("** Class name missing **")
        elif args not in HBNBCommand.class_list:
            print("** Class doesn't exist **")
        else:
            _a = eval(args)()
            print(_a.id)
            _a.save()

    def do_show(self, args):
        """Prints The String Representation Of An Instance Based
        On The Class Name And Id"""
        _sw = 0
        _arg = args.split()
        if args == "":
            print("** Class name missing **")
        elif _arg[0] not in HBNBCommand.class_list:
            print("** Class doesn't exist **")
        elif len(_arg) < 2:
            print("** Instance id missing **")
        else:
            in_key = (_arg[0] + "." + _arg[1])
            for _key, _obj in storage.all().items():
                if _key == in_key:
                    print(_obj)
                    _sw = 1
            if _sw == 0:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        updating JSON file\nUsage: (hbnb) destroy <class_name> <class_id>"""
        _sw = 0
        arg = args.split()
        if args == "":
            print("** Class name missing **")
        elif arg[0] not in HBNBCommand.class_list:
            print("** Class doesn't exist **")
        elif len(arg) < 2:
            print("** Instance id missing **")
        else:
            in_key = (arg[0] + "." + arg[1])
            dict_objects = storage.all()
            for _key, _obj in dict_objects.items():
                if _key == in_key:
                    del dict_objects[_key]
                    _sw = 1
                    storage.save()
                    storage.reload()
                    return
            if _sw == 0:
                print("** no instance found **")

    def do_all(self, args):
        """Prints All String Representation Of All Anstances
        Based Or Not On The Class Name"""
        list_ = []
        if args == "":
            for _key, _obj in storage.all().items():
                list_.append(str(_obj))
            print(list_)
        elif args in HBNBCommand.class_list:
            for _key, _obj in storage.all().items():
                if args == _key.split(".")[0]:
                    list_.append(str(_obj))
            print(list_)
        else:
            print("** Class doesn't exist **")

    def do_update(self, args):
        """Updates An instance Based On The Class Name And Id by Adding or
        Updating Attribute, Saving On JSON File"""
        _arg = args.split()
        _sw = 0
        if len(_arg) < 1:
            print("** Class name missing **")
        elif arg[0] not in HBNBCommand.class_list:
            print("** Class doesn't exist **")
        elif len(_arg) < 2:
            print("** Instance id missing **")
        elif len(_arg) < 3:
            print("** Attribute name missing **")
        elif len(_arg) < 4:
            print("** Value missing **")
        else:
            in_key = (_arg[0] + "." + _arg[1])
            for _key, _obj in storage.all().items():
                if _key == in_key:
                    _idx_arg = len(_arg[0]) + len(_arg[1]) + len(_arg[2]) + 3
                    _value = args[_idx_arg:]
                    if args[_idx_arg] == "\"":
                        _idx_arg += 1
                        _value = args[_idx_arg:-1]
                    if hasattr(_obj, _arg[2]):
                        _value = type(getattr(_obj, _arg[2]))(args[_idx_arg:])
                    setattr(_obj, _arg[2], _value)
                    _sw = 1
                    storage.save()
            if _sw == 0:
                print("** No instance found **")
                return -1

    def default(self, args):
        """Default Method That Perfom Actions When No Command It's Given"""
        count = 0
        if len(args.split(".")) > 1:
            class_name = args.split(".")[0]
            if class_name in HBNBCommand.class_list:
                try:
                    if args.split(".")[1] == "all()":
                        self.do_all(_class_name)
                    if args.split(".")[1] == "count()":
                        for _key, _obj in storage.all().items():
                            if _key.split(".")[0] == class_name:
                                count += 1
                        print(count)
                    if args.split(".")[1].split("(")[0] == "show":
                        id_ = args.split("\"")[1].split("\"")[0]
                        self.do_show(_class_name + " " + id_)
                    if args.split(".")[1].split("(")[0] == "destroy":
                        id_ = args.split("\"")[1].split("\"")[0]
                        self.do_destroy(_class_name + " " + id_)
                    if args.split(".")[1].split("(")[0] == "update":
                        arg_list = args.split(".", 1)[1]
                        arg_list = arg_list.split("(")[1][:-1].split(",")
                        if "{" not in arg_list[1]:
                            id_ = arg_list[0][1:-1]
                            name = arg_list[1][2:-1]
                            value = arg_list[2][1:]
                            if value[0] == "\"":
                                value = value[1:-1]
                            self.do_update(class_name + "\
 " + id_ + " " + name + " " + value)
                        else:
                            id_ = arg_list[0][1:-1]
                            arg_dict = args.split(".")[1]
                            arg_dict = arg_dict.split("(")[1][:-1]
                            arg_dict = arg_dict.split("{")[1]
                            arg_dict = "{" + arg_dict
                            dictionary = eval(arg_dict)
                            for _key, _value in dictionary.items():
                                ret = self.do_update(_class_name + "\
 " + id_ + " " + _key + " " + str(value))
                                if ret == -1:
                                    break
                except Exception:
                    cmd.Cmd.default(self, args)
        else:
            cmd.Cmd.default(self, args)


if __name__ == "__main__":
    comand = HBNBCommand()
    comand.cmdloop()
