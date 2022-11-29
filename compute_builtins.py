import numpy as np

prices = [ 12.2, 34.1, 45.1, 24.1, 2.4 ]

total_price = sum(prices)
print("Total:", total_price, "€")
print(f"Total: {total_price:0.2f}€")

# generator expression (better than list comprehension list here)
total_square_price = sum(p**2 for p in prices)
print("Total p^2:", total_square_price)

# numpy: broadcast operator (**2)
prices_np = np.array(prices)
total_square_price = sum(prices_np**2)
print("Total p^2:", total_square_price)

# min/max
min_price = min(prices)
max_price = max(prices)
print(f"Min: {min_price:0.2f}€ ; Max: {max_price:0.2f}€")

cities = ["Toulouse", "Bordeaux", "Versailles", 
        "Pau", "Blagnac", "Tournefeuille"]
min_city = min(cities)
print("Min city ( str <):", min_city)


# sort/sorted
sorted_prices = sorted(prices)
print("Sorted prices (asc)", sorted_prices)
sorted_prices_desc = sorted(prices, reverse=True)
print("Sorted prices (desc)", sorted_prices_desc)

words_es = ["mañana","mano", "matador"]
# sort => new list
words_es_sorted = sorted(words_es)
print(words_es_sorted)
# sort in place
words_es.sort()
print(words_es)
# TODO: apply spanish rules

words_fr = ["été", "étage", "étuve"]
words_fr.sort()
print(words_fr)
# TODO: apply french rules

cities_dict = [
        {
            'name': 'Toulouse',
            'pop': 470000
        },
        {
            'name': 'Versailles',
            'pop': 80000
        },
        {
            'name': 'Pau',
            'pop': 77000
        },
        {
            'name': 'Bordeaux',
            'pop': 250000
        },
    ]
print(cities_dict)

def key_pop(city_dict):
    return city_dict['pop']

cities_sorted_by_pop_asc = sorted(cities_dict, key=key_pop)
print("Cities (pop asc):", cities_sorted_by_pop_asc)

cities_sorted_by_pop_desc = sorted(cities_dict, key=key_pop, reverse=True)
print("Cities (pop desc):", cities_sorted_by_pop_desc)







