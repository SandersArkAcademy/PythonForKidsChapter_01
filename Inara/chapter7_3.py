#Programming puzzles 1

def moon_weight(OGearth_weight, OGearth_weightIncrease):
   # OGearth_weight = 38.6
    moon_Converstion_Factor = 0.165
    for year in range(0,15):
        earth_weight = OGearth_weight + (year * OGearth_weightIncrease)
        moon_weight = earth_weight * moon_Converstion_Factor
        print('Year:%s Earth weight: %sKg Moon weight:%sKg' %(year +1,earth_weight,moon_weight))


moon_weight(38.6,1)