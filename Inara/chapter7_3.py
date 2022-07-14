#Programming puzzles 2

def moon_weight(OGearth_weight, OGearth_weightIncrease,num_Years_to_Run):
   
    MOON_CONVERSION_FACTOR = 0.165
    for year in range(0,num_Years_to_Run):
        earth_weight = OGearth_weight + (year * OGearth_weightIncrease)
        moon_weight = earth_weight * MOON_CONVERSION_FACTOR
        print('Year:%s Earth weight: %sKg Moon weight:%sKg' %(year +1,earth_weight,moon_weight))


moon_weight(38.6,1,15)