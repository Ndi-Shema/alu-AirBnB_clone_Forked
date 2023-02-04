import unittest

""" testing the file storage"""
from models.engine.file_storage import FileStorage


class TestCaseFileStorage(unittest.TestCase):
    """ class for test cases """

    def setUp(self):
        """ setting up the various
            components for the test """
        self.my_model = FileStorage()

    def test_all(self):
        self.assertEqual(type(self.my_model.all()), dict)
