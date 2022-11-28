from decimal import Decimal

print("Hello")
print('A lot of traffic this morning')

for i in range(10):
    print(i)

print("The end")

# str (text)
city = "Toulouse"
# int (integer), no limit
temperature = 9
# float
# https://fr.wikipedia.org/wiki/IEEE_754
pression = 1000.3
price = 0.1 # 0.000110011001100..
print(price, 2*price, 3*price)
total = 3*price

# format strings
# https://docs.python.org/3/library/string.html#formatstrings
print(f"Total: {total:0.2f}€") # python 3.6
print("Total: {:0.2f}€".format(total)) # python 3
print("Total: %s" % total) # old way


priceExact = Decimal('0.1')
print(priceExact, 2*priceExact, 3*priceExact)