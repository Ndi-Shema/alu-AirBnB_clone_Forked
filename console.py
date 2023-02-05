#!/usr/bin/python3
""" console interpreter """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    existing_classes = ['BaseModel', 'User', 'City',
                        'State', 'Place', 'Review', 'Amenity', '']
    prompt = "(hbnb)"
    # test = BaseModel()
    # print(test)

    def emptyline(self):
        """ called when empty line
        is entered in response """
        pass

    def do_quit(self, argv):
        """exit - Exit Applicaiton"""
        return True

    def do_EOF(self, argv):
        """ end of file """
        print("")
        return True

    def do_create(self, new_class):
        """ Creates a new instance of Basemodel
        saves it(to the JSON file) and prints the id"""
        if not new_class:
            print("** class name missing **")
        else:
            if new_class not in self.existing_classes:
                # print(self.existing_classes)
                print("** class doesn't exist **")
            else:
                new_class = eval(new_class + "()")
                new_class.save()
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
            if items[0] not in self.existing_classes:
                print("** class doesn't exist **")
            else:
                if (len(items)) < 2:
                    print("** instance id missing **")
                else:

                    # storage.reload()
                    # loaded_data = storage.all()
                    # print(loaded_data)
                    try:
                        # print("key is {}".format(items[0] + "." + items[1]))
                        class_found = storage.all()[items[0] + "." + items[1]]
                        # new_class_found = BaseModel(class_found)
                        # print(new_class_found)
                        print(class_found)
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

    def do_destroy(self, *argv):
        """Deletes an instance based on the class name and id
        (saves the changes into the json file) """

        items = argv[0].split(" ")
        if (len(items)) == 1 and items[0] == '':
            print("** class name missing **")
        else:
            if items[0] not in self.existing_classes:
                print("** class doesn't exist **")
            else:
                if (len(items)) < 2:
                    print("** instance id missing **")
                else:
                    # storage.reload()
                    # loaded_data = storage.all()
                    # print(loaded_data)
                    try:
                        # print("key is {}".format(items[0] + "." + items[1]))
                        del storage.all()[items[0] + "." + items[1]]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")

    def do_all(self, class_type):
        """ prints all string representation of all instances based
        or not on the class name """
        if class_type not in self.existing_classes:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            # print(type(all_objects))
            # print(all_objects)
            for key, value in enumerate(all_objects):
                #   print(" key = {} , value = {}".format(key, value))
                out = all_objects[value]
                if class_type == out.__class__.__name__:
                    print(out)

    def do_update(self, *argv):
        """ updates an instance based on the class\
         name and id by adding or updating
        attribute ( save the change into the json file)"""
        items = argv[0].split(" ")

        if (len(items)) == 1 and items[0] == '':
            print("** class name missing **")
        else:
            if items[0] not in self.existing_classes:
                print("** class doesn't exist **")
            else:
                if (len(items)) < 2:
                    print("** instance id missing **")
                else:
                    # storage.reload()
                    # loaded_data = storage.all()
                    # print(loaded_data)
                    try:
                        # print("key is{}".format(items[0]+"."+items[1]))
                        # del loaded_data[items[0] + "." + items[1]]
                        temp_dict = storage.all()[items[0] + "." + items[1]]
                        if (len(items)) < 3:
                            print("** attribute name missing **")
                        else:
                            if(len(items)) == 3:
                                print("** value missing **")
                            elif (len(items)) == 4:
                                # get the attribute specified and update it
                                if type(items[3]) in [str, float, int]:
                                    # set attr build in function
                                    txt = items[3]
                                    temp_dict.__dict__[items[2]] = txt[1:-1]
                                    # print(temp_dict.__dict__)
                                    # setattr(temp_dict, items[2], txt[1:-1])
                                    temp_dict.save()

                    except KeyError:
                        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
