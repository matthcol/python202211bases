# list
cities = [ "Toulouse", "Versailles", "Pau", "Bordeaux" ]
print(cities)

# loops
for city in cities:
    print("\t-", city)

for city in cities:
    print(city,' -> ', sep='', end='')
print()

print(cities, sep=' -> ') # print one arg: list
print(*cities, sep=' -> ') # print all elements in list
print("Toulouse", "Versailles", "Pau", "Bordeaux", sep=' -> ')

for letter in "Toulouse":
    print(letter, end=' ')
print()

print("1er (index 0):",cities[0])
print("Dernier (index length -1):",cities[len(cities)-1])
print("Dernier (index -1):",cities[-1])
#print(cities[4]) # IndexError: list index out of range
#print(cities[-5]) # IndexError: list index out of range

# print city names + indexes with a for loop
# somes ideas: index (cost!), range, enumerate
for i in range(len(cities)):
    print("\t*", i, cities[i])
print()

# better, isn't it ?
for i, city in enumerate(cities):
    print("\t~", i, city)
print()

# start with 1 not 0
for i, city in enumerate(cities, 1):
    print("\t°", i, city)
print()

city = {
    'name': 'Toulouse',
    'pop': 471941,
    'cp': '31000' 
    }

print(city)
print(city['name'])


for k in city: # i.e. city.keys()
    print("Key -> Value:", k, city[k])
print()

for info in city.values():
    print("Value:", info)
print()

for key, value in city.items():
    print("Key, Value:", key, value)
print()


# other loop: while

# conditional: if, case

