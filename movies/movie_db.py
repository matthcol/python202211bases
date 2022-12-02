from movie import Movie
from typing import List

def save_movie(movie: Movie):
    pass


def get_movies_by_year_range_title_containing(
        year1: int, year2: int, title_part: str) -> List[Movie]:
    pass


m = Movie("Prey", 2021, 99)
save_movie(m)

save_movie("Top Gun: Maverick")

l = get_movies_by_year_range_title_containing(1950, 1988, 'Star')
for m in l:
    print(m.title)

# check hints on this program with mypy
# mypy movie_db.py
