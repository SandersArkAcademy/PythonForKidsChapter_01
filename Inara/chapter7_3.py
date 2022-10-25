#Programming puzzles 3

import sys

def moon_weightASK():
    print('Please enter your current Earth weight in kilograms.')
    OGearth_weight = float(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year in kilograms')
    OGearth_weightIncrease= float(sys.stdin.readline())
    print('Please enter the number of years')
    num_Years_to_Run = int(sys.stdin.readline())
    moon_weight(OGearth_weight,OGearth_weightIncrease,num_Years_to_Run)

def moon_weight(OGearth_weight, OGearth_weightIncrease,num_Years_to_Run):
   
    MOON_CONVERSION_FACTOR = 0.165
    for year in range(0,num_Years_to_Run):
        earth_weight = OGearth_weight + (year * OGearth_weightIncrease)
        moon_weight = earth_weight * MOON_CONVERSION_FACTOR
        print('Year:%s Earth weight: %sKg Moon weight:%sKg' %(year +1,earth_weight,moon_weight))


moon_weightASK()