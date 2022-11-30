# use builtin function open
# default: read, text mode
with open('data/cafes-concerts.csv', encoding='UTF-8') as f:
    # f is iterable on its rows

    # exo1: print row with word MORILLES
    word = 'MORILLES'
    for row in f:
        if word in row:
            print(row)

# f.close() auto (scenario normal or error)
print("Check f is closed:", f.closed)

# exo2: afficher le nom des bars
sep=';'
with open('data/cafes-concerts.csv', encoding='UTF-8') as f:
    # skip first line with headers
    next(f)
    # inspect fllowing rows
    for row in f:
        words = row.split(sep)
        print("Café concert:", words[2])

# for advances search, use module re

# better solution: module csv (python) or pandas (the best)


# in write mode, use w, x or a
with open('data/coucou.txt', mode='a') as f_out:
    f_out.write('Coucou\n')

# NB: in binary mode, user rb, wb, ...
