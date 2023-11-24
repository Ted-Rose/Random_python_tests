"""
    Made following NeuralNine video:
    https://www.youtube.com/watch?v=Qb4rMvFRLJw
"""

from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def print_data():
        """ implement in child class """

class PersonSingleton(IPerson):

    __instance__ = None

    @staticmethod
    def get_instance():
        # If no instance created yet for PersonSingleton
        if PersonSingleton.__instance__ is None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance__
        # We need to ensure that this constructor cannot be
        # used multiple times - to avoid overwriting the instance

    def __init__(self, name, age):
        # You can raise exception or anything else if there
        # is instance already
        if PersonSingleton.__instance__ is not None:
            raise Exception("Singleton cannot be implemented more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance__ = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance__.name},\
             age: {PersonSingleton.__instance__.age}")

p = PersonSingleton("Mike", 30)
print(p)
p.print_data()

# If instantiated twice returns exception:
# Exception("Singleton cannot be implemented more than once!")
# p = PersonSingleton("Bob", 25)

# Gets the same instance
p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()