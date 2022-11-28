import euclide as euc

def test_gcd_primes():
    a = 2
    b = 7
    g = euc.gcd(a, b)
    assert g == 1
    
def test_gcd_12():
    a = 60
    b = 204
    g = euc.gcd(a, b)
    assert g == 12