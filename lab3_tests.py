import io
import sys
import unittest
from unittest.mock import MagicMock
from lab3 import ConcreteCreator1, ConcreteCreator2, client_code


class TestClientCode(unittest.TestCase):
    def setUp(self):
        self.creator1 = ConcreteCreator1()
        self.creator2 = ConcreteCreator2()

    def test_client_code_with_creator1(self):
        self.creator1.factory_method = MagicMock(
            return_value=MagicMock(operation=MagicMock(return_value="Mocked Result")))
        expected_output = "Client: I'm not aware of the creator's class, but it still works.\nCreator: The same creator's code has just worked with Mocked Result"


        captured_output = io.StringIO()
        sys.stdout = captured_output
        client_code(self.creator1)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_client_code_with_creator2(self):
        self.creator2.factory_method = MagicMock(
            return_value=MagicMock(operation=MagicMock(return_value="Mocked Result")))
        expected_output = "Client: I'm not aware of the creator's class, but it still works.\nCreator: The same creator's code has just worked with Mocked Result"


        captured_output = io.StringIO()
        sys.stdout = captured_output
        client_code(self.creator2)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()
