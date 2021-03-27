#Author: Drew Rafferty
def getMovies():
    movies = []

    try:
        with open("exercises/march28/movies.txt") as file:
            for line in file:
                movie = line.replace("\n", "")
                movies.append(movie)
    except:
        print("File could not be located")

    return movies

print("*** Awesome Movie Program ***")
movies = getMovies()

for movie in movies:
    print(movie)