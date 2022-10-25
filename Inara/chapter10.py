import turtle
t = turtle.Pen()

class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color

harry = Animal('hippogriff', 6, 'pink')

import copy
harry = Animal('hippogriff', 6, 'pink')
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)

harry = Animal('hippogriff', 6, 'pink')
carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('bogsill', 0, 'paisley')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[1].species)

my_animals[0].species = 'ghoul'
print(my_animals[0].species)

sally = Animal('sphinx', 4, 'sand')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))

more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'wyrm'
print(my_animals[0].species)
print(more_animals[0].species)

import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('ozwald'))
print(keyword.kwlist)

import random
print(random.randint(1, 100))
print(random.randint(100, 1000))
print(random.randint(1000, 5000))