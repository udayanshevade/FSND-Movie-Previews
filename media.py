class Media(object):
    """Contains useful info about a movie or tv show.

    Attributes:
        title: the title of the specified media
        poster_image_url: a path to the media poster image
        description: a brief synopsis of the media
        video_id: the id of the link to the YouTube trailer
        url = the link to the tmdb page
        genres = a list of applicable genres
        rating = the voting average from users
        votes = the count of user votes
    """

    def __init__(
        self,
        title,
        poster_image_url,
        description,
        video_id,
        url,
        genres,
        rating,
        votes
    ):
        """Inits Media class with specified movie parameters"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.description = description
        self.video_id = video_id
        self.url = url
        self.genres = genres
        self.rating = rating
        self.votes = votes


class Movie(Media):
    """Contains useful info about a movie.

    Attributes:
        title: the title of the specified movie
        poster_image_url: a path to the movie poster image
        description: a brief synopsis of the movie
        video_id: the id of the link to the YouTube trailer
        url = the link to the tmdb page
        tagline = the movie tagline
        genres = a list of applicable genres
        rating = the voting average from users
        votes = the count of user votes
    """

    def __init__(
        self,
        title,
        poster_image_url,
        description,
        video_id,
        url,
        tagline,
        genres,
        rating,
        votes
    ):
        """Inits Movie class with specified movie parameters"""
        super(Movie, self).__init__(
            title,
            poster_image_url,
            description,
            video_id,
            url,
            genres,
            rating,
            votes
        )
        self.tagline = tagline


class Show(Media):
    """Contains useful info about a tv show.

    Attributes:
        title: the title of the specified show
        poster_image_url: a path to the show poster image
        description: a brief synopsis of the show
        video_id: the id of the link to the YouTube trailer
        url = the link to the tmdb page
        genres = a list of applicable genres
        rating = the voting average from users
        votes = the count of user votes
    """
    def __init__(
        self,
        title,
        poster_image_url,
        description,
        video_id,
        url,
        genres,
        rating,
        votes
    ):
        """Inits Show class with specified movie parameters"""
        super(Show, self).__init__(
            title,
            poster_image_url,
            description,
            video_id,
            url,
            genres,
            rating,
            votes
        )
