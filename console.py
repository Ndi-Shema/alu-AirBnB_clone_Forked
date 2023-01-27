#!/usr/bin/python3
""" console interpreter """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    # test = BaseModel()
    # print(test)

    @staticmethod
    def do_quit(self):
        """exit - Exit Applicaiton"""
        return True

    @staticmethod
    def help_quit(self):
        """help for quit here"""
        print('Quit command to exit the program')

    def do_create(self, new_class):
        """ Creates a new instance of Basemodel
        saves it(to the JSON file) and prints the id"""
        if not new_class:
            print("** class name missing **")
        else:
            new_class = BaseModel()
            if new_class.__class__.__name__ != "BaseModel":
                print("** class doesn't exist **")
            else:
                # print(new_class)
                new_class.save()
                # print(new_class)
                print(new_class.__dict__['id'])

    def do_show(self, *argv):
        """ Prints the string representation of an instance based on
        the class name and id """

        # print(type(argv))
        # print(argv[0][0])
        # print(argv)
        items = argv[0].split(" ")
        # print(items)
        # print("the Len is {}".format(len(items)))
        # print(len(items))

        # print(args[0])

        if (len(items)) == 1 and items[0] == '':
            print("** class name missing **")
        else:
            if (len(items)) < 2:
                print("** instance id missing **")
            else:
                data_class = FileStorage()
                data_class.reload()
                loaded_data = data_class.all()
                # print(loaded_data)
                try:
                    print("key is {}".format(items[0] + "." + items[1]))
                    class_found = loaded_data[items[0] + "." + items[1]]
                    if class_found['__class__'] != "BaseModel":
                        print("** class doesn't exist **")
                    else:
                        new_class_found = BaseModel(class_found)
                        print(new_class_found)
                except KeyError:
                    print("** no instance found **")

                # if loaded_data[items[0] + "." + items[1]] is None:
                #    print("** no instance found **")
                # else:
                #   class_found = loaded_data[items[0] + "." + items[1]]
                #    if class_found.__class__.__name__ != "BaseModel":
                #        print("** class doesn't exist **")
                #    else:
                #        print(class_found)

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
