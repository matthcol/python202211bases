import magicsquare as ms

def test_magic_sum_3():
    res = ms.magic_sum(3)
    assert res == 15 

def test_magic_sum_5():
    res = ms.magic_sum(5)
    assert res == 65

square3_ok = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8],
    ]

square3_ko_row = [
        [2, 3, 6],
        [9, 5, 1],
        [4, 7, 8],
    ]

def test_is_magic_square_row_ok():
    res = ms.is_magic_square_row(square3_ok)
    assert res is True

def test_is_magic_square_row_ko():
    res = ms.is_magic_square_row(square3_ko_row)
    assert res is False
