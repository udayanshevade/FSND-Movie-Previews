class Movie(object):
    """Contains useful info about a movie.

    Attributes:
        title: the title of the specified movie
        poster_image_url: a path to the movie poster image
        description: a brief synopsis of the movie
        trailer_youtube_id: the id of the link to the YouTube trailer
        imdb_url = the link to the imdb page
        tagline = the movie tagline
    """

    def __init__(
        self,
        title,
        poster_image_url,
        description,
        trailer_youtube_id,
        imdb_url,
        tagline
    ):
        """Inits Movie class with specified info"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.description = description
        self.trailer_youtube_id = trailer_youtube_id
        self.imdb_url = imdb_url
        self.tagline = tagline
