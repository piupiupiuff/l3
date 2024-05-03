class Product:
    def show(self):
        pass

class ConcreteProduct1(Product):
    def show(self):
        print("Concrete Product 1")

class ConcreteProduct2(Product):
    def show(self):
        print("Concrete Product 2")

class Creator:
    def factory_method(self):
        pass

    def operation(self):
        product = self.factory_method()
        product.show()

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()


creator1 = ConcreteCreator1()
creator1.operation()

creator2 = ConcreteCreator2()
creator2.operation()
