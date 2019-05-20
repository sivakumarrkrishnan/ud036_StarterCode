# creating  a class named Movie


class Movie():
    """encapsulate the movie properties - Title, movie poster and a trailer."""
    def __init__(self, movie_title, movie_poster, movie_trailer):
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer