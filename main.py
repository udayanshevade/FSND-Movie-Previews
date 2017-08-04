import webbrowser
import os
import re
import tmdbsimple as tmdb
import media
from env import env

# Specify an API_KEY for the request to work
tmdb.API_KEY = "e82675e3ce7ac55822d324d26d627295"


def get_movies_data(movie_ids):
    """Fetches movie data using a wrapper for the TMDB API.
       Compiles a list of movie instances
       which will be rendered dynamically."""
    print("Fetching movie data...")
    poster_base = "https://image.tmdb.org/t/p/w300{picture_id}"
    url_base = "https://themoviedb.org/movie/{id}"
    movies = []
    # Request data per API id in list
    for id in movie_ids:
        movie = tmdb.Movies(id)
        # get the details associated with the movie
        movie.info()

        # Some context for the wait time.
        print("Getting data for {}".format(movie.title))

        # get poster image src
        poster_url = poster_base.format(picture_id=movie.poster_path)

        # make a secondary request for trailer videos
        videos_res = movie.videos()
        videos = videos_res["results"]
        video_id = None if not len(videos) else videos[0]["key"]

        url = url_base.format(id=movie.id)

        movies.append(media.Movie(
            movie.title,
            poster_url,
            movie.overview.encode("ascii", "ignore"),
            video_id,
            url,
            movie.tagline,
            [genre["name"] for genre in movie.genres],
            movie.vote_average,
            movie.vote_count
        ))
    return movies


def get_shows_data(show_ids):
    """Fetches show data using a wrapper for the TMDB API.
       Compiles a list of show instances
       which will be rendered dynamically."""
    print("Fetching show data...")
    poster_base = "https://image.tmdb.org/t/p/w300{picture_id}"
    url_base = "https://themoviedb.org/tv/{id}"
    shows = []
    # Request data per API id in list
    for id in show_ids:
        show = tmdb.TV(id)
        show.info()

        # context while waiting
        print ("Getting data for {}".format(show.name))

        # get poster image src
        poster_url = poster_base.format(picture_id=show.poster_path)

        # make secondary request for trailer videos
        videos_res = show.videos()
        videos = videos_res["results"]
        video_id = None if not len(videos) else videos[0]["key"]

        url = url_base.format(id=show.id)


        shows.append(media.Show(
            show.name,
            poster_url,
            show.overview.encode("ascii", "ignore"),
            video_id,
            url,
            [genre["name"] for genre in show.genres],
            show.vote_average,
            show.vote_count
        ))
    return shows


def create_media_content(movies, shows):
    """The HTML content for this section of the page"""
    print("Populating templates...")
    media_tile_template = env.get_template('media_tile.html')
    movies_content = create_movie_tiles_content(movies, media_tile_template)
    shows_content = create_show_tiles_content(shows, media_tile_template)
    return movies_content, shows_content


def create_show_tiles_content(shows, template):
    """HTML content for shows"""

    content = ''
    for show in shows:
        # Append the tile for the show with its content filled in
        content += template.render({
            "title": show.title,
            "poster_image_url": show.poster_image_url,
            "video_id": show.video_id,
            "description": show.description,
            "url": show.url,
            "genres": show.genres,
            "rating": show.rating,
            "votes": show.votes
        })
    return content


def create_movie_tiles_content(movies, template):
    """HTML content for movies"""

    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += template.render({
            "title": movie.title,
            "poster_image_url": movie.poster_image_url,
            "video_id": movie.video_id,
            "description": movie.description,
            "url": movie.url,
            "tagline": movie.tagline,
            "genres": movie.genres,
            "rating": movie.rating,
            "votes": movie.votes
        })
    return content


def open_movies_page(movie_ids, show_ids):
    """Triggers data request and injects data into html"""
    print("Loading...")
    shows = get_shows_data(show_ids)
    movies = get_movies_data(movie_ids)
    movies_content, shows_content = create_media_content(movies, shows)

    # Creates or overwrites generated html
    output_file = open('index.html', 'w')

    main_page_template = env.get_template('page.html')
    trailer_modal_content = env.get_template('trailer_modal.html').render()
    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_template.render({
        "trailer_modal_content": trailer_modal_content,
        "movie_tiles": movies_content,
        "show_tiles": shows_content
    })

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # Opens the output file in the browser (in a new tab)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
