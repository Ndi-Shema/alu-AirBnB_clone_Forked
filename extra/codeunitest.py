#!/usr/bin/python3
# code checks if a number is even or odd
"""code checks on whether a number is even or odd"""
import sys


def check(num_one):
    """ checks if a number is even or odd
        argument : num_one
        return : strings """
    if num_one % 2 == 0:
        return "even"
    else:
        return "odd"


# print(check(int(sys.argv[1])))
