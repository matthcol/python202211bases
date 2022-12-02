import operator as op
import functools as fun

# See also: properties, @dataclass

@fun.total_ordering
class Movie:
    """class representing an object movie with its title, year, duration (opt)"""
    
    def __init__(self, title, year, duration=None):
        """constructor"""
        self.title = title
        self.year = year
        self.duration = duration

    def __repr__(self):
        """repr and str override"""
        return f"{self.title} ({self.year})"

    def __len__(self):
        """len override"""
        # return self.duration # Error if duration is None
        return self.duration if self.duration is not None else 0

    def __eq__(self, other):
        """ override == and != 
        NB: deactivate __hash__
        """ 
        if not isinstance(other, Movie):
            return NotImplemented
        return (self.title, self.year) == (other.title, other.year)

    def __lt__(self, other):
        """ override < operator
            Example:
                movie1 < movie2
        """
        if not isinstance(other, Movie):
            return NotImplemented
        return (self.year, self.title) < (other.year, other.title)
        

if __name__ == '__main__':
    m0 = Movie("Z", 1969)
    m1 = Movie('E.T.', 1982)
    m2 = Movie('Tenet', 2020, duration=150)
    m3 = Movie("The Lion King", 1994)
    m4 = Movie("Pulp Fiction", 1994)
    m5 = Movie("The Lion King", 2019)
    m6 = Movie("Léon", 1994)
    movies = [m0, m1, m2, m3, m4, m5, m6]
    for m in movies:
        print("\t-", m, "; length:", len(m))
    print("m1 == m2 ?", m1 == m2)
    # sort with internal <
    movies.sort()
    print(movies)
    # sort by title only with key: m => m.title
    movies.sort(key=lambda m: m.title)
    print(movies)
    movies.sort(key=op.attrgetter('title'))
    print(movies)
    # other order comparisons
    print(f"{m1} > {m2}", m1 > m2)
    print(f"{m1} <= {m2}", m1 <= m2)
    print(f"{m1} >= {m2}", m1 >= m2)


