import webbrowser
import os
import re
import tmdbsimple as tmdb
import media
from jinja2 import Template, Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader('fresh_tomatoes', 'static/templates')
)


# Specify an API_KEY for the request to work
tmdb.API_KEY = "e82675e3ce7ac55822d324d26d627295"


def get_movies_data(movie_ids):
    """Fetches data using a wrapper for the TMDB API.
       Compiles a list of movie instances
       which will be rendered dynamically."""
    print("Fetching movie data...")
    poster_base = "http://image.tmdb.org/t/p/w300{picture_id}"
    imdb_base = "http://imdb.com/title/{imdb_id}"
    movies = []
    for id in movie_ids:
        movie = tmdb.Movies(id)
        # get the details associated with the movie
        response = movie.info()

        print("Getting data for {}".format(movie.title))

        # get poster image src
        poster_url = poster_base.format(picture_id=movie.poster_path)

        # get any trailer videos
        videos = movie.videos()
        video_id = videos["results"][0]["key"]

        imdb_url = imdb_base.format(imdb_id=movie.imdb_id)
        movies.append(media.Movie(
            movie.title,
            poster_url,
            movie.overview,
            video_id,
            imdb_url,
            movie.tagline
        ))
    return movies


def create_movie_tiles_content(movies):
    """The HTML content for this section of the page"""
    print("Populating templates...")
    movie_tile_template = env.get_template('movie_tile.html')
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += movie_tile_template.render({
            "movie_title": movie.title,
            "poster_image_url": movie.poster_image_url,
            "trailer_youtube_id": movie.trailer_youtube_id,
            "movie_description": movie.description,
            "imdb_url": movie.imdb_url,
            "tagline": movie.tagline
        })
    return content


def open_movies_page(movie_ids):
    """Makes data request and writes data to the html"""
    print("Loading...")
    movies = get_movies_data(movie_ids)

    # Creates or overwrites generated html
    output_file = open('fresh_tomatoes.html', 'w')

    main_page_template = env.get_template('page.html')
    trailer_modal_content = env.get_template('trailer_modal.html').render()
    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_template.render({
            "trailer_modal_content": trailer_modal_content,
            "movie_tiles": create_movie_tiles_content(movies)
        })

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # Opens the output file in the browser (in a new tab)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
