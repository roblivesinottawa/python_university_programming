class Movie:
    MOVIE_TYPES = ("COMEDY", "DRAMA", "ACTION", "SCI-FI")
    __movielist = None

    @staticmethod
    def getmovielist():
        if Movie.__movielist == None:
            Movie.__movielist = []
        return Movie.__movielist

    @classmethod
    def getmovietypes(cls):
        return cls.MOVIE_TYPES

    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, movietype):
        self.title = title
        if (not movietype in Movie.MOVIE_TYPES):
            raise ValueError(f"{movietype} is not a valid movie type")
        else:
            self.movietype = movietype

print(f"Movie types: {Movie.getmovietypes()}")

movie1 = Movie("Title 1", "COMEDY")
movie2 = Movie("Title 2", "DRAMA")

themovies = Movie.getmovielist()
themovies.append(movie1)
themovies.append(movie2)
print(themovies)