from media import Movie
import main
from random import shuffle

# List of TMDB database ids
movie_ids = ["1417", "313369", "62", "14160", "38", "348"]
# Unique order every time compiled
shuffle(movie_ids)

# Dynamically generate page
main.open_movies_page(movie_ids)
