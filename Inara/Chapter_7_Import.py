# Chapter 7 Import

import sys
#print(sys.stdin.readline())

def silly_age_joke():
    print('How old are you?')
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
     print('What is 13 + 49 + 84 + 155 + 97? A headache!')
    else:
        print('Huh?')

silly_age_joke()