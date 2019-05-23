class Door:
    color = ''
    
    def __init__(self, color):
        self.color = color

class House:
    door = None
    area = 0
    description = ''
    
    def __init__(self, door, area):
        self.door = door
        self.area = area
        self.description = 'a house'
    
    def describe(self):
        return 'a ' + `self.area` + 'm2 ' + self.description + ' with ' + self.door.color + ' doors'

class Apartment(House):
    def __init__(self, door):
        self.door = door
        self.area = 50
        self.description = 'an apartment'

class Person:
    name = ''
    home = None

    def __init__(self, name, home):
        self.name = name
        self.home = home

    def describe(self):
        return 'My name is ' + self.name + ' and I live in ' + self.home.describe() + '.'

door = Door('black')
house = House(door, 75)
apartment = Apartment(door)

person1 = Person('John', house)
person2 = Person('Mary', apartment)

print(person1.describe())
print(person2.describe())