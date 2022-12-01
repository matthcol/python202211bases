import movie
import pytest

text = "not a movie"
m = movie.Movie("The Lion King", 1994)
mAllDifferent = movie.Movie("Tenet", 2020)
mSameTitle = movie.Movie("The Lion King", 2019)
mSameYear = movie.Movie("Léon", 1994)
mSameTitleYear = movie.Movie("The Lion King", 1994)


def test_eq_reflexive():
    assert (m == m) is True

def test_ne_reflexive():
    assert (m != m) is False

def test_eq_heterogeneous_left():
    res = m == text
    assert res is False

def test_eq_heterogeneous_right():
    res = text == m
    assert res is False

def test_ne_heterogeneous_left():
    res = m != text
    assert res is True

def test_ne_heterogeneous_right():
    res = text != m
    assert res is True

def test_eq_same_title_year():
    res = m == mSameTitleYear
    assert res is True


@pytest.mark.parametrize("other", [
    mSameTitle, mSameYear, mAllDifferent
])
def test_eq_different_left(other):
    res = m == other
    assert res is False

@pytest.mark.parametrize("other", [
    mSameTitle, mSameYear, mAllDifferent
])
def test_eq_different_right(other):
    res = other == m
    assert res is False