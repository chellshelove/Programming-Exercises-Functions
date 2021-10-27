def calc_weight_on_planet(weight, surfaceGravity = 23.1): #the function has 2 arguments, where surfaceGravity is optional and also has a default number
    return (weight / 9.8) * surfaceGravity #formula of the updated weight

updatedWeight1 = calc_weight_on_planet(120,9.8) #120 is the weight of the earth and 9.8 is the surface gravity of the planet
print("calc_weight_on_planet(120,9.8)") #the results should be 120.0
print(updatedWeight1)

updatedWeight2 = calc_weight_on_planet(120) #120 is the weight of the earth and 23.1 is the surface gravity of the planet
print("calc_weight_on_planet(120)") #the results should be 282.85714285714283 even if the value of 23.1 is opted out
print(updatedWeight2)

updatedWeight3 = calc_weight_on_planet(120,23.1) #120 is the weight of the earth and 23.1 is the surface gravity of the planet
print("calc_weight_on_planet(120,23.1)") #the results should be 282.85714285714283
print(updatedWeight3)