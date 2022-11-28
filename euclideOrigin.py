# Algorithme d'Euclide (PGCD)
# https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide

a = 15
b = 12

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
    
print("Gcd is:", a)