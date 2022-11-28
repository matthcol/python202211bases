import pytest
import euclide as euc
from typing import Tuple

@pytest.fixture(params=[
    (3, 5, 1),
    (2, 7, 1),
    (12, 15, 3),
    (15, 12, 3),
    (204, 60, 12),
])
def abg(request):
    return request.param

def test_pgcd(abg: Tuple[int, int, int]):
    a, b, expect_gcd = abg
    actual_gcd = euc.gcd(a, b)
    assert expect_gcd == actual_gcd 
    