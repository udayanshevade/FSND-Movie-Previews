from media import Movie
import fresh_tomatoes

# List of TMDB database ids
movie_ids = ["1417", "313369", "62", "14160", "38", "348"]

# Dynamically generate page
fresh_tomatoes.open_movies_page(movie_ids)
