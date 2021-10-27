def num_atoms(grams, weight = 196.97): #the function has 2 arguments, where weight is optional and also has a default number
    mole = weight / grams #formula for the mole
    avogadro = (6.022 * 10 ** 23) / mole #formula for the avogadro
    print(avogadro)

print("num_atoms(10)") #10 is the grams of the atom and 196.97 is the atomic weight of the gold
num_atoms(10) #the results should be 3.0573183733563486e+22

print("num_atoms(10, 12.001)") #10 is the grams of the atom and 12.001 is the atomic weight of the gold
num_atoms(10, 12.001) #the results should be 5.017915173735522e+23

print("num_atoms(10, 1.008)") #10 is the grams of the atom and 1.008 is the atomic weight of the gold
num_atoms(10, 1.008) #the results should be 5.974206349206349e+24