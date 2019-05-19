import fresh_tomatoes
import media

# creating an instance named "avengers" for the Movie class and instantiating the movie objects
avengers = media.Movie("Avengers Endgame", \
                        "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg", \
                        "https://www.youtube.com/watch?v=TcMBFSGVi1c")


# creating an instance named "dumbo" for the Movie class
dumbo = media.Movie("Dumbo",  \
                        "https://upload.wikimedia.org/wikipedia/en/9/91/Dumbo_%282019_film%29.png", \
                        "https://www.youtube.com/watch?v=7NiYVoqBt-8")

# creating an instance named "how_to_train" for the Movie class
how_to_train = media.Movie("How to Train Your Dragon",  \
                        "https://upload.wikimedia.org/wikipedia/en/f/fd/How_to_Train_Your_Dragon_3_poster.png", \
                        "https://www.youtube.com/watch?v=CQ7XUCQ6pbE")

# creating an instance named "captain_marvel" for the Movie class
captain_marvel = media.Movie("Captain Marvel",  \
                        "https://upload.wikimedia.org/wikipedia/en/8/85/Captain_Marvel_poster.jpg", \
                        "https://www.youtube.com/watch?v=Z1BCujX3pw8")

# storing all the instances created in a list
movies = [avengers, dumbo, how_to_train, captain_marvel]


# calling the open_movies_page() function with the list of movies as input
# in order to display the trailer website.
fresh_tomatoes.open_movies_page(movies)