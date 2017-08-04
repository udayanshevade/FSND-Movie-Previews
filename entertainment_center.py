from media import Movie
import main
from random import shuffle

# List of TMDB database movie ids
movie_ids = ["129", "1417", "313369", "62", "14160", "38", "348", "9323"]
# List of TMDB database movie ids
show_ids = ["30991", "1396", "31911", "1438", "246", "4546", "1399", "60694"]
# Unique order every time compiled
shuffle(movie_ids)
shuffle(show_ids)

# Dynamically generate page
main.open_movies_page(movie_ids, show_ids)
