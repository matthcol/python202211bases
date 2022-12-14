import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data to download here:
# https://data.toulouse-metropole.fr/explore/dataset/cafes-concerts/export/
coffees = pd.read_csv('data/cafes-concerts.csv', sep=';')
print(coffees)

x = np.linspace(0, 2*np.pi, 10000)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, 'r', x, z, 'b', linestyle='dashed', linewidth=2)
plt.show()

