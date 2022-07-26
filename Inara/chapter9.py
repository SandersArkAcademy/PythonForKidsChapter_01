from doctest import testfile
import numbers
from operator import le


print(abs(10))
print(abs(-10))

steps = -3
if abs(steps) > 0:
    print('Character is moving')

steps = -3
if steps < 0 or steps > 0:
    print('Character is moving')

print(bool(0))
print(bool(1))
print(bool(1123.23))
print(bool(-500))

print(bool(None))
print(bool('a'))
print(bool(' '))
print(bool('What do you call a pig doing karate? Pork Chop!'))

my_silly_list = []
print(bool(my_silly_list))
my_silly_list = ['s', 'i', 'l', 'l', 'y']
print(bool(my_silly_list))

year = input('Year of birth:')
if not bool(year.rstrip()):
    print('You need to enter a value for your year of birth')

dir(['a', 'short', 'list'])
dir(1)
popcorn = 'I love popcorn!'
dir(popcorn)
help(popcorn.upper)

eval('10*5')

your_calculation = input('Enter a calculation:')
eval(your_calculation)

my_small_program = '''print('ham')
print('sandwich')'''
exec(my_small_program)

float('12')

float('123.456789')

your_age = input('Enter your age: ')

age = float(your_age)
if age > 13:
    print('You are %s years too old' % (age - 13))

int(123.456)

len('this is a test string')

#%%
creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon', 'troll']
print(len(creature_list))

#%%
enemies_map = {'Batman' : 'Joker', 'Superman' : 'Lex Luthor', 'Spiderman' : 'Green Goblin'}
print(len(enemies_map))

#%%
fruit = ['apple', 'bannana', 'clementine', 'dragon fruit']
length = len(fruit)
for x in range(0, length):
    print('the fruit at index %s is %s' % (x, fruit[x]))
#%%
numbers = [5, 4, 10, 30, 22]
print(max(numbers))
# %%
strings = 's,t,r,i,n,g,S,T,R,I,N,G'
print(max(strings))
# %%
print(max(10, 300, 450, 50, 90))
# %%
numbers = [5, 4, 10, 30, 22]
print(min(numbers))
# %%
guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
    print('Boom! You all lose')
else:
    print('You win')
# %%
for x in range(0,5):
    print(x)
# %%
print(list(range(0, 5)))
# %%
count_by_twos = list(range(0, 30, 2))
print(count_by_twos)
# %%
my_list_of_numbers = list(range(0, 500, 50))
print(my_list_of_numbers)
print(sum(my_list_of_numbers))
# %%
testfile = open('./test.txt')
#"C:\Users\inara\OneDrive\Documents\GitHub\PythonForKidsChapter_01\Inara\test.txt"
text = testfile.read()
print(text)
testfile.close()
# %%
test_file = open('./test.txt', 'a')
#"C:\Users\inara\OneDrive\Documents\GitHub\PythonForKidsChapter_01\Inara\test.txt"
test_file.write('What is green and loud? A froghorn!')
test_file.close()
test_file = open('./test.txt', 'r')
text5 = test_file.read()
#text5.split(' ')
print(text5)
test_file.close()
# %%
