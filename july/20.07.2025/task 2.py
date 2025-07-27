from abc import ABC, abstractclassmethod

class Animal(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def say(self):
        pass
        # print("Звук животного")

class Cat(Animal):
    def say(self):
        print("Мяу")

class Dog(Animal):
    def say(self):
        print("Гав")

class Cow(Animal):
    pass

# _animal = Animal()
_cat = Cat()
_dog = Dog()
_cow = Cow()

_cat.say()
_dog.say()
_cow.say() 