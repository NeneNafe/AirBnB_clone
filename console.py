#!/usr/bin/python3
"""
python command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class that inherits from the Cmd class and does command line commands"""
    prompt = '(hbnb) '

    def do_EOF(self, *args):
        """End of file command"""
        return True

    def do_quit(self, *args):
        """Quit command to exit the program\n"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
