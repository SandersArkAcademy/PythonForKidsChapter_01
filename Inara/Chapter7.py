#%%
list(range(0,5))
# %%
list(range(0,1000))
# %%
def testfunc(myname):
    print('hello %s' % myname)
# %%
testfunc('Mary')
# %%
def testfunc(fname, lname):
    print('Hello %s %s' % (fname, lname))
# %%
testfunc('Mary', 'Smith')
# %%
firstname = 'Joe'
lastname = 'Robertson'
testfunc(firstname, lastname)
# %%
def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending
# %%
print(savings(10, 10, 5))
# %%
def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable
# %%
print(variable_test())
# %%
# I did do the example but got rid of it so it would not count it wrong.
# %%
another_variable = 100
def variable_test2():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable * another_variable
 
# %%
print(variable_test2())
# %%
def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Week %s = %s cans' % (week, total_cans))
# %%
spaceship_building(2)
# %%
spaceship_building(13)
# %%
import time
print(time.asctime())
# %%
import sys
print(sys.stdin.readline())
# %%
def silly_age_joke(age):
    if age >= 10 and age <= 13:
        print('What is 13 + 49 + 84 + 155 + 97? A headache!')
    else:
        print('Huh?')

# %%
silly_age_joke(9)
# %%
silly_age_joke(10)
# %%
def silly_age_joke():
    print('How old are you?')
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('What is 13 + 49 + 84 + 155 + 97? A headache!')
    else:
        print('Huh?')
# %%
silly_age_joke(10)
# %%
silly_age_joke(15)
# %%
