from calendar import month
import sys
#v = sys.stdin.readline()
#He who laughs last thinks slowest
#print(v)

#v = sys.stdin.readline(13)
#He who laughs last thinks slowest
#print(v)
#These commands appears to only work in the Python shell

sys.stdout.write("What does a fish say when it swims into a wall? Dam.")

print(sys.version)

import time
print(time.time())

def lots_of_numbers(max):
    for x in range(0, max):
        print(x)
lots_of_numbers(1000)

def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print('it took %s seconds' % (t2-t1))
lots_of_numbers(1000)

print(time.asctime())

t = (2007, 5, 27, 10, 30, 48, 6, 0, 0)

t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))

print(time.localtime())

t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)

for x in range(1, 61):
    print(x)
    time.sleep(1)

game_data = {'player-position' : 'N23 E45', 'pockets' : ['keys', 'pocket knife', 'polished stone'], 'backpack' : ['rope', 'hammer', 'apple'], 'money' : 158.50}
