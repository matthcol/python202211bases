import magicsquare as ms
import pytest

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

square3_ko_column = [
        [2, 7, 6],
        [1, 5, 9],
        [4, 3, 8],
    ]

square3_ko_diag = [
        [9, 5, 1],
        [2, 7, 6],
        [4, 3, 8],
    ]

square3_ko_not_all_numbers_repeat_one = [
        [5,5,5],
        [5,5,5],
        [5,5,5],
]

square3_ko_not_all_numbers_too_high = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 10],
]

square3_ko_not_all_numbers_too_low = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 0, 8],
]

def test_is_magic_square_row_ok():
    res = ms.is_magic_square_row(square3_ok)
    assert res is True

def test_is_magic_square_row_ko():
    res = ms.is_magic_square_row(square3_ko_row)
    assert res is False

def test_is_magic_square_column_ok():
    res = ms.is_magic_square_column(square3_ok)
    assert res is True

def test_is_magic_square_column_ko():
    res = ms.is_magic_square_column(square3_ko_column)
    assert res is False

def test_is_magic_square_diagonal_ok():
    res = ms.is_magic_square_diagonal(square3_ok)
    assert res is True

def test_is_magic_square_diagonal_ko():
    res = ms.is_magic_square_diagonal(square3_ko_diag)
    assert res is False

def test_is_magic_square_all_present_ok():
    res = ms.is_magic_square_all_present(square3_ok)
    assert res is True


@pytest.mark.parametrize("square_ko", [
        square3_ko_not_all_numbers_repeat_one,
        square3_ko_not_all_numbers_too_high,
        square3_ko_not_all_numbers_too_low
])
def test_is_magic_square_all_present_ko(square_ko):
    res = ms.is_magic_square_all_present(square_ko)
    assert res is False

# Test Integration
@pytest.mark.parametrize("square_ok", [
    square3_ok,
    # square4_albrecht_durer,
    # square8_general_cazalas
])
def test_is_magic_ok(square_ok):
    res = ms.is_magic_square(square_ok)
    assert res is True

@pytest.mark.parametrize("square_ko", [
    square3_ko_row,
    square3_ko_column,
    square3_ko_diag,
    square3_ko_not_all_numbers_repeat_one,
    square3_ko_not_all_numbers_too_high,
    square3_ko_not_all_numbers_too_low
])
def test_is_magic_ok(square_ko):
    res = ms.is_magic_square(square_ko)
    assert res is False

