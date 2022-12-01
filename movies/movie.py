class Movie:
    
    def __init__(self, title, year, duration=None):
        """constructor"""
        self.title = title
        self.year = year
        self.duration = duration

    def __repr__(self):
        return f"{self.title} ({self.year})"

if __name__ == '__main__':
    m1 = Movie('E.T.', 1982)
    print(m1)
    m2 = Movie('Tenet', 2020, duration=150)
    print(m2)