class Cat:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def info(self):
        return self.name, self.age

    def sound(self):
        return print(self.name, " makes sound meow")

class Dog:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def info(self):
        return self.name, self.age

    def sound(self):
        return print(self.name, " makes sound woof")

c1 = Cat("pussy", 3)
# print(c1.info())
# c1.sound()

c2 = Dog("Tom", 3)
# print(c2.info())
# c2.sound()

def pet(pet):
    print(pet.info())
    pet.sound()

print(pet(c2))

