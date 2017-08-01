class Movie(object):
    """Contains useful info about a movie.

    Attributes:
        title: the title of the specified movie
        poster_image_url: a path to the movie poster image
        description: a brief synopsis of the movie
        trailer_youtube_url: a link to the YouTube trailer
    """

    def __init__(
        self,
        title,
        poster_image_url,
        description,
        trailer_youtube_url
    ):
        """Inits Movie class with specified info"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.description = description
        self.trailer_youtube_url = trailer_youtube_url
