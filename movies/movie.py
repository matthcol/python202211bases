class Movie:
    
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
        """ override == and != """ 
        if not isinstance(other, Movie):
            return NotImplemented
        return (self.title, self.year) == (other.title, other.year)

if __name__ == '__main__':
    m1 = Movie('E.T.', 1982)
    m2 = Movie('Tenet', 2020, duration=150)
    movies = [m1, m2]
    for m in movies:
        print("\t-", m, "; length:", len(m))
    print("m1 == m2 ?", m1 == m2)