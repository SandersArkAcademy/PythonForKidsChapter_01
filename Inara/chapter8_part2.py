class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    pass
class Mammals(Animals):
    pass
class Giraffes(Mammals):
    pass

reginald = Giraffes()

def this_is_a_normal_function():
    print('I am a normal function')

class ThisIsMySillyClass:
    def this_is_a_class_function():
        print('I am a class function')
    def this_is_also_a_class_function():
        print('I am also a class function. See?')

class Animals(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass

class Mammals(Animals):
    def feed_young_with_milk(self):
        pass

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass

reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

harold = Giraffes()
harold.move()

class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')

reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees()