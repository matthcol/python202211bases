
def magic_sum(n):
    """ Compute magic sum of a square of size n.
        Use formula n(n^2+1)/2
    """
    return n * (n**2 + 1) // 2

def is_magic_square_row(square):
    """ check if all rows are magic
    """
    n = len(square)
    ms = magic_sum(n)
    for row in square:
        row_sum = sum(row)
        if row_sum != ms:
            return False
    return True


def is_magic_square_column(square):
    """ check if all columns are magic
    """
    n = len(square)
    ms = magic_sum(n)
    for j in range(n):
        # compute sum over column j
        # * sol1: recode sum
        # column_sum = 0
        # for i in range(n):
        #     column_sum += square[i][j]
        # * sol2: use sum
        column_sum = sum(square[i][j] for i in range(n))
        # check sum is magic
        if column_sum != ms:
            return False
    return True



def is_magic_square_diagonal(square):
    """ check if both 'diagonals' are magic
    """
    n = len(square)
    ms = magic_sum(n)
    # diagonal 1 (main)
    # NB: you can use sum + for expr here
    diag_sum = 0
    for i in range(n):
        diag_sum += square[i][i]
    if diag_sum != ms:
        return False
    # diagonal 2 (symetric)
    # NB: you can use sum + for expr here
    diag_sum = 0
    for i in range(n):
        diag_sum += square[i][n-1-i]
    if diag_sum != ms:
        return False
    return True

def is_magic_square_all_present(square):
    """ check if all numbers between 1 and n^2 are used 
    (only once)"""
    n = len(square)
    numbers = list(range(1,n**2+1))
    for i in range(n):
        for j in range(n):
            if square[i][j] in numbers:
                numbers.remove(square[i][j])
            else:
                return False
    return len(numbers) == 0

def is_magic_square(square):
    """ check if all rules are verified to be a magic square
    """
    return (is_magic_square_row(square)
        and is_magic_square_column(square)
        and is_magic_square_diagonal(square)
        and is_magic_square_all_present(square))
