import pickle
game_data = {'player-position' : 'N23 E45', 'pockets' : ['keys', 'pocket knife', 'polished stone'], 'backpack' : ['rope', 'hammer', 'apple'], 'money' : 158.50}
save_file = open('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()

load_file = open('save.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()
print(loaded_game_data)

import copy
class Car:
    pass

car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)
# It will print the number 3
car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)
# It will print the number 3 again
