from media import Movie
import fresh_tomatoes


# We compile a list of movie instances
# which will be rendered dynamically
# using the function open_movies_page
# from the fresh_tomatoes module.
movies = [
    Movie("Pan's Labyrinth",
          "https://upload.wikimedia.org/wikipedia/en/6/67/Pan%27s_Labyrinth.jpg",  #noqa
          "This is a description of the movie.",
          "https://www.youtube.com/watch?v=EXe5a9pBNzg"),
    Movie("2001: A Space Odyssey",
          "https://upload.wikimedia.org/wikipedia/en/a/a7/2001_A_Space_Odyssey_%281968%29_theatrical_poster_variant.jpg",  # noqa
          "This is a description of the movie",
          "https://www.youtube.com/watch?v=XHjIqQBsPjk"),
    Movie("Eternal Sunshine of the Spotless Mind",
          "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",  # noqa
          "This is a description of the movie.",
          "https://www.youtube.com/watch?v=quuMv7cGUn0"),
    Movie("Alien",
          "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",  # noqa
          "This is a description of the movie.",
          "https://www.youtube.com/watch?v=LjLamj-b0I8"),
    Movie("Up",
          "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",  #noqa
          "This is a description of the movie.",
          "https://www.youtube.com/watch?v=ORFWdXl_zJ4"),
    Movie("La La Land",
          "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  #noqa
          "This is a description of the movie.",
          "https://www.youtube.com/watch?v=ORFWdXl_zJ4")
]

fresh_tomatoes.open_movies_page(movies)
