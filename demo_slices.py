city = "Toulouse"
cities = ["Toulouse", "Bordeaux", "Versailles", 
        "Pau", "Blagnac", "Tournefeuille"]

print("First 3 letters:", city[0:3])
print("First 3 letters:", city[:3]) # first index is not mandatory
print("Letters at indexes 3,4,5:", city[3:6])
print("Letters from index 5 to the end:", city[5:])
print("Last 3 letters:", city[-3:])
print("After data:", city[25:4000])

# replace cities at indexes 3,4 by Bayonne, Balma
print("Cities (start):", cities)
cities[3:5] = ["Bayonne", "Balma"]
print("Cities (replace 3,4):", cities)
# remove cities 3,4
# sol1: 
# del cities[3:5]
# sol2
cities[3:5] = []
print("Cities (delete 3,4):", cities)
# insert Pau, Bagnac at index 0
cities[0:0] = ["Pau", "Blagnac"]
print("Cities (insert at 0):", cities)

# with methods
cities.insert(0, "Marseille")
cities.append("Montpellier")
cities.extend(("Barcelone", "Berlin", "Londres")) # ou list ou any iterable
print("After insert/append/extend:", cities)

# slices with step:  start:stop:step
print("each 2 cities (even index)", cities[::2])
print("each 2 cities (odd index)", cities[1::2])

print("city (reversed word):", city[::-1])
print("last 3 cities (reverser order)", cities[:-4:-1])

# slices can be expressed with builtin function slice()
print("last 3 cities (reverser order)", cities[slice(None,-4,-1)])

# reverse every city word in list cities => new list
# sol 1 (oldschool way)
cities_reversed = []
for city in cities:
    cities_reversed.append(city[::-1])
print("Reversed cities:", cities_reversed)

# sol 2 (comprehension list)
cities_reversed = [ city[::-1] for city in cities ]
print("Reversed cities:", cities_reversed)

# comprehension list with filter
cities_starting_with_T_reversed = [ 
        city[::-1] 
        for city in cities 
        if city.startswith('T') 
    ]
print("Reversed cities wtarting with T:", 
        cities_starting_with_T_reversed)

x = 3
y = (x + 3) * 4 / x + x**2 \
    * 1.000000000000000000000000000000000000000000000000000000000000000001 \
    + 1
print("y:", y)