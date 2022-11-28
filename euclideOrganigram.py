# Algorithme d'Euclide (PGCD)
# https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide

a = 15
b = 12

while b != 0:
    r = a % b
    a, b = b, r
    
print("Gcd is:", a)