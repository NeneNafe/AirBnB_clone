#!/usr/bin/python3
"""
python command interpreter
"""
import cmd
import json
from models import storage
from models import *


class HBNBCommand(cmd.Cmd):
    """class that inherits from the Cmd class and does command line commands"""
    prompt = '(hbnb) '

    def do_EOF(self, *args):
        """End of file command"""
        return True

    def do_quit(self, *args):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file"""
        if line:
            # checks if the line is not empty from the storage class
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                # creates an instance of the given class
                new_instance = storage.classes()[line]()
                new_instance.save()
                print(new_instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the str representstion of an instance
        """
        if not line:
            print("** class name missing **")
        else:
            # splits the args passed to the console
            cmd_args = line.split(" ")
            # checks if the command takes two args
            if cmd_args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(cmd_args) < 2:
                print("** instance id missing **")
            else:
                key = f"{cmd_args[0]}.{cmd_args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            cmd_args = line.split(" ")
            if cmd_args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(cmd_args < 2):
                print("** instance id missing **")
            else:
                key = f"{cmd_args[0]}.{cmd_args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
