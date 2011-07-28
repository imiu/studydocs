class Animal(object):
    pass

class Dog(Animal):
    """docstring for Dog"""
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    """docstring for Cat"""
    def __init__(self, name):
        self.name = name

class Person(object):
    """docstring for Person"""
    def __init__(self, name):
        self.name = name

        self.pet = None

class Employee(Person):
    """docstring for Employee"""
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")
satan = Cat("Satan")

mary = Person("Mary")
mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
