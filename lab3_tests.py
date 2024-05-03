import unittest
import logging

class Product:
    def show(self):
        pass

class ConcreteProduct1(Product):
    def show(self):
        logging.info("Concrete Product 1")

class ConcreteProduct2(Product):
    def show(self):
        logging.info("Concrete Product 2")

class Creator:
    def factory_method(self):
        pass

    def operation(self):
        product = self.factory_method()
        if product is not None:
            product.show()
        else:
            raise NotImplementedError("factory_method() must be implemented in subclass.")

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

class TestFactoryMethod(unittest.TestCase):
    def test_concrete_creator1_operation(self):
        creator1 = ConcreteCreator1()
        with self.assertLogs() as logs:
            creator1.operation()
        self.assertEqual(logs.output, ['INFO:root:Concrete Product 1'])

    def test_concrete_creator2_operation(self):
        creator2 = ConcreteCreator2()
        with self.assertLogs() as logs:
            creator2.operation()
        self.assertEqual(logs.output, ['INFO:root:Concrete Product 2'])

    def test_creator_operation_without_factory_method(self):
        creator = Creator()
        with self.assertRaises(NotImplementedError):
            creator.operation()

    def test_concrete_product1_show(self):
        product1 = ConcreteProduct1()
        with self.assertLogs() as logs:
            product1.show()
        self.assertEqual(logs.output, ['INFO:root:Concrete Product 1'])

    def test_concrete_product2_show(self):
        product2 = ConcreteProduct2()
        with self.assertLogs() as logs:
            product2.show()
        self.assertEqual(logs.output, ['INFO:root:Concrete Product 2'])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
