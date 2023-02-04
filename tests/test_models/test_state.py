import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def test_instance(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_is_class(self):
        state = State()
        self.assertEqual(str(type(state)),
                         "<class 'models.state.State'>")

    def test_is_subclass(self):
        state = State()
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_state_name(self):
        state = State()
        state.name = "Rwanda"
        self.assertEqual(state.name, 'Rwanda')

    if __name__ == "__main__":
        unittest.main()
