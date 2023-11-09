#!/usr/bin/python3
"""
python command interpreter
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel


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
            all_objs = storage.all()
            if line not in all_objs():
                print("** class doesn't exist **")
            else:
                # creates an instance of the given class
                model_class = all_objs[line].__class__
                new_instance = model_class()
                new_instance.save()
                print(new_instance.id)
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
