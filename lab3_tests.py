import unittest
from io import StringIO
from unittest.mock import patch

from lab3 import ConcreteCreator1, ConcreteCreator2


class TestCreator(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()

    def tearDown(self):
        self.output.close()

    def test_concrete_creator1_operation(self):
        creator1 = ConcreteCreator1()
        with patch('sys.stdout', new=self.output) as fake_out:
            creator1.operation()
            self.assertEqual(fake_out.getvalue().strip(), "Concrete Product 1")

    def test_concrete_creator2_operation(self):
        creator2 = ConcreteCreator2()
        with patch('sys.stdout', new=self.output) as fake_out:
            creator2.operation()
            self.assertEqual(fake_out.getvalue().strip(), "Concrete Product 2")


if __name__ == '__main__':
    unittest.main()
