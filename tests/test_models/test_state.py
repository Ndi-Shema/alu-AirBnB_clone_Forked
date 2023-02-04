import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_instance(self):
        self.assertIsInstance(self.state, State)

    def test_is_class(self):
        self.assertEqual(str(type(self.state)),
                         "<class 'models.state.State'>")

    def test_is_subclass(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_state_name(self):
        self.state.name = "Rwanda"
        self.assertEqual(self.state.name, 'Rwanda')

    if __name__ == "__main__":
        unittest.main()
