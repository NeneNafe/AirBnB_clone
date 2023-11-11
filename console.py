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

    def do_EOF(self, line):
        """End of file command"""
        return True

    def do_quit(self, line):
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
            elif len(cmd_args) < 2:
                print("** instance id missing **")
            else:
                key = f"{cmd_args[0]}.{cmd_args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances"""
        cmd_args = line.split(" ")
        if not line:
            print("** class name is missing **")
        elif cmd_args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            instances = []
            for key, value in storage.all().items():
                # Cheks if the key belongs to the specified class
                class_name, instance_id = key.split('.')
                if class_name == cmd_args[0]:
                    instances.append(str(value))
            print(instances)

    def do_update(self, line):
        """ Updates an instance based on the class name and id"""
        cmd_args = line.split(" ")

        if not line:
            print("** class name missing **")
        elif cmd_args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(cmd_args) < 2:
            print("** instance id missing **")
        else:
            key = f"{cmd_args[0]}.{cmd_args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            elif len(cmd_args) < 3:
                print("** attribute name missing **")
            elif len(cmd_args) < 4:
                print("** value missing **")
            else:
                instance = storage.all()[key]
                attribute_name = cmd_args[3]
                attribue_value = cmd_args[4]

                # checks if the attribute_name is not one that is restricted
                if attribute_name in ("id", "created_at", "updated_at"):
                    print("** can't be update id, created_at, upsated_at **")
                else:
                    # it gets the attribute type fro the instance
                    attr_type = type(getattr(instance, attribute_name, None))
                    # The You cast the attr value to the correct type
                    try:
                        casted_value = attr_type(attribue_value)
                    except ValueError:
                        print(f"** invalid value for {attribute_name} **")
                        return
                    # Then You update the attribute and save the changes
                    setattr(instance, attribute_name, casted_value)
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
