#!/usr/bin/python3
""" console interpreter """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    test = BaseModel()
    print(test)

    def do_quit(self, inpu):
        '''exit - Exit Applicaiton'''
        return True

    def help_quit(self):
        '''help for quit here'''
        print('Quit command to exit the program')

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
