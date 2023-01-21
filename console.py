#!/usr/bin/python3
""" console interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, inpu):
        '''exit - Exit Applicaiton'''
        return True

    def help_quit(self):
        '''help for quit here'''
        print('Quit command to exit the program')

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
