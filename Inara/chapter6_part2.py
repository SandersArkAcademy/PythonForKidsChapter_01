#%%
from operator import truediv


for x in range(0,5):
    print('hello')

#%%
print(list(range(10, 20)))
# %%
for x in range(0,5):
    print('hello %s' % x)
# %%
wizard_list = ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']

for i in wizard_list:
    print(i)
# %%
hugehairypants = ['huge', 'hairy', 'pants']
for i in hugehairypants:
    print(i)
    print(i)
# %%
hugehairypants = ['huge', 'hairy', 'pants']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
            print(j)
# %%
for x in range(0, 20):
    print('hello %s' % x)
    if x < 9:
        break
# %%
x = 1
while x < 13:
    x = x + 2
    print(x)

#%%
for step in range(0, 20):
    print(step)

# %%
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'catipillar eyebrows', 'centepede toes']
ingredient_1 = 'snails'
ingredient_2 = 'leeches'
ingredient_3 = 'gorilla belly-button lint'
ingredient_4 = 'catipillar eyebrows'
ingredient_5 = 'centepede toes'
ingredients_list = ingredient_1
for x in range(1, 6):
    ingredients_list = ingredients_list + ingredient_2 + ingredient_3 + ingredient_4 + ingredient_5
    print('%s' % x, ingredients_list)
# %%
ingredients = ['1 snails'
'2 leeches'
'3 gorilla belly-button lint'
'4 catipillar eyebrows'
'5 centepede toes']
for x in range(1, 2):
    print('%s' % x, ingredients)
# %%
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'catipillar eyebrows', 'centepede toes']
counter = 1
for index in ingredients:
    print('%s %s' %(counter,index))
    counter= counter +1

# %%
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'catipillar eyebrows', 'centepede toes']
for i in range(0,5):
    print('%s %s' % (i+1,ingredients[i]))

# %%
OGearth_weight = 38.6
for year in range(0,15):
    earth_weight = OGearth_weight + (year * 1)
    moon_weight = earth_weight * 0.165
    print('Year:%s Earth weight: %sKg Moon weight:%sKg' %(year +1,earth_weight,moon_weight))
# %%
