import random
from sqlite3.dbapi2 import _SingleParamWindowAggregateClass
desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
print(random.choice(desserts))

desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
random.shuffle(desserts)
print(desserts)

import sys
sys.exit()
#This function will exit the Python shell, it does not work in Visual Studio Code.
