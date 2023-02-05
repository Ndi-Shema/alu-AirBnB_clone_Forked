#!/usr/bin/python3
""" testing states"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        """ setup for test """
        self.state = State()

    def test_instance(self):
        """ test instance type """
        self.assertIsInstance(self.state, State)

    def test_is_class(self):
        """ test class """
        self.assertEqual(str(type(self.state)),
                         "<class 'models.state.State'>")

    def test_is_subclass(self):
        """ test is sub class """
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_state_name(self):
        """ test mainly state name """
        self.state.name = "Rwanda"
        self.assertEqual(self.state.name, 'Rwanda')
        self.assertIsNotNone(self.state.id)

    if __name__ == "__main__":
        unittest.main()
